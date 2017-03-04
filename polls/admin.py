from django.contrib import admin
from .models import Question, Choice, Questionnaire, QuestionQuestionnaire, ReponseQuestionnaires, ReponseQuestionQuestionnaire


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
# end class


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	list_max_show_all = 10
	list_per_page = 5
# end class

class QuestioneInline(admin.TabularInline):
	model = QuestionQuestionnaire
	extra = 3
# end class

class QuestionnaireAdmin(admin.ModelAdmin):
	fieldsets = [
		('Identification',               {'fields': ['label']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [QuestioneInline]
	list_display = ('label', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['label']
	list_max_show_all = 10
	list_per_page = 5
# end class


admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
