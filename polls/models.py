import datetime

from django.db import models
from django.utils import timezone

###############
### SONDAGE ###
###############

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date de publication')
	def __str__(self):
		return self.question_text
	# end def
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	# end def

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Publié récemment?'
# end class

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
	# end def
# end class

class Reponse(models.Model):
	nom = models.CharField(max_length=50, default="Anonyme")
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
	def __str__(self):
		return self.nom+" - "+self.question.question_text+" - "+self.choice.choice_text
	# end def
# end class


#####################
### QUESTIONNAIRE ###
#####################

class Questionnaire(models.Model):
	label = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Date de publication')
	def __str__(self):
		return self.label
	# end def
# end class

class QuestionQuestionnaire(models.Model):
	question = models.CharField(max_length=200)
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	def __str__(self):
		return self.question
	# end def
# end class

class ReponseQuestionnaires(models.Model):
	nom = models.CharField(max_length=50, default="Anonyme")
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	date = models.DateTimeField('Date de reponse')
	def __str__(self):
		return self.nom+" - "+self.questionnaire.label
	# end def
# end class

class ReponseQuestionQuestionnaire(models.Model):
	question = models.CharField(max_length=200)
	reponse = models.CharField(max_length=200)
	reponse_questionnaire = models.ForeignKey(ReponseQuestionnaires, on_delete=models.CASCADE)
	def __str__(self):
		return self.reponse_questionnaire.nom+" - "+self.reponse_questionnaire.questionnaire.label+" - "+self.question
	# end def
# end class


