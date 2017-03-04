from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Reponse
from .models import Questionnaire, QuestionQuestionnaire, ReponseQuestionnaires, ReponseQuestionQuestionnaire

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	queryset = Question.objects.all()
	
	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context['latest_questionnaire_list'] = Questionnaire.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
		context['latest_sondage_list'] = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
		return context
	# end def 
# end class

class IndexSondageView(generic.ListView):
	template_name = 'polls/indexSondage.html'
	context_object_name = 'sondages'
	def get_queryset(self):
		#Retourne les 5 dernières questions publiées
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
	# end def
# end class

class IndexQuestionnaireView(generic.ListView):
	template_name = 'polls/indexQuestionnaire.html'
	context_object_name = 'questionnaires'
	def get_queryset(self):
		#Retourne les 5 dernières questions publiées
		return Questionnaire.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
	# end def
# end class


#############
## SONDAGE ##
#############

class DetailSondageView(generic.DetailView):
	model = Question
	template_name = 'polls/detailSondage.html'
	def get_queryset(self):
		#Exclus toutes les questions qui n'ont pas encore été publiées
		return Question.objects.filter(pub_date__lte=timezone.now())
	# end def
# end class

class ResultsSondageView(generic.DetailView):
	model = Question
	template_name = 'polls/resultsSondage.html'
# end class

def voteSondage(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redirection vers la question avec le message d'erreur.
		return render(request, 'polls/detailSondage.html', {
			'question': question,
			'error_message': "Vous n'avez pas séléctionné de choix.",
		})
	else:
		#Enregistre le vote de la personne dans le choix
		selected_choice.votes += 1
		selected_choice.save()

		#Enregistre la reponse de la personne
		reponse = Reponse()
		nom = request.POST['nom']
		if nom != '' :
			reponse.nom = nom
		reponse.question = question
		reponse.choice = selected_choice
		reponse.save()

		#Redirection vers la page des résultats
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	# end try
# end def

###################
## QUESTIONNAIRE ##
###################

class DetailQuestionnaireView(generic.DetailView):
	model = Questionnaire
	template_name = 'polls/detailQuestionnaire.html'
	def get_queryset(self):
		#Exclus tous les questionnaires qui n'ont pas encore été publiés
		return Questionnaire.objects.filter(pub_date__lte=timezone.now())
	# end def
# end class

class ResultsQuestionnaireView(generic.DetailView):
	model = Questionnaire
	template_name = 'polls/resultsQuestionnaire.html'
# end class

def reponseQuestionnaire(request, questionnaire_id):
	# Récupération du questionnaire
	questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)	
	
	# Création de la reponse au questionnaire
	reponseQuest = ReponseQuestionnaires()
	nom = request.POST['nom']
	if nom != '' :
		reponseQuest.nom = nom
	else :
		reponseQuest.nom = "Anonyme"
	# end if
	reponseQuest.date = timezone.now()
	reponseQuest.questionnaire = questionnaire
	reponseQuest.save()
	
	# Parcours de toutes les questions du formulaire pour récupérer les réponses
	for question in questionnaire.questionquestionnaire_set.all():
		reponse = request.POST.get("reponse"+str(question.id),False)
		if (reponse != False):			
			reponseQuestQuest = ReponseQuestionQuestionnaire()
			reponseQuestQuest.question = question
			reponseQuestQuest.reponse = reponse
			reponseQuestQuest.reponse_questionnaire = reponseQuest
			reponseQuestQuest.save()
		# end if
	# end for
	
	#Redirection vers la page des résultats
	return HttpResponseRedirect(reverse('polls:resultsQuestionnaire', args=(questionnaire.id,)))
# end def

###################
## GENERTION PDF ##
###################
    
