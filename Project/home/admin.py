from django.contrib import admin
from .models import Question,Answer

class QuestionAdmin(admin.ModelAdmin):
	list_display  = ['question','date','upvotes']
	list_filter   = ['date']
	search_fields = ['question']

class AnswerAdmin(admin.ModelAdmin):
	list_display  = ['answer','edit_date','upvotes']
	list_filter   = ['edit_date']
	search_fields = ['answer']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)

