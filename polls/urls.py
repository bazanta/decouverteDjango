from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^sondages$', views.IndexSondageView.as_view(), name='indexSondage'),
	url(r'^questionnaires$', views.IndexQuestionnaireView.as_view(), name='indexQuestionnaire'),
	
	url(r'^sondages/(?P<pk>[0-9]+)/$', views.DetailSondageView.as_view(), name='detail'),
	url(r'^sondages/(?P<pk>[0-9]+)/results/$', views.ResultsSondageView.as_view(), name='results'),
	url(r'^sondages/(?P<question_id>[0-9]+)/vote/$', views.voteSondage, name='vote'),
	
	url(r'^questionnaires/(?P<pk>[0-9]+)/$', views.DetailQuestionnaireView.as_view(), name='detailQuestionnaire'),
	url(r'^questionnaires/(?P<pk>[0-9]+)/results/$', views.ResultsQuestionnaireView.as_view(), name='resultsQuestionnaire'),
	url(r'^questionnaires/(?P<questionnaire_id>[0-9]+)/reponse/$', views.reponseQuestionnaire, name='reponseQuestionnaire'),	
]


