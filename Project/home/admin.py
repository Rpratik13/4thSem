from django.contrib import admin
from .models import Question,Answer,Vote

class QuestionAdmin(admin.ModelAdmin):
	list_display  = ['question','date']
	list_filter   = ['date']
	search_fields = ['question']
	
class AnswerAdmin(admin.ModelAdmin):
	list_display  = ['answer','edit_date']
	list_filter   = ['edit_date']
	search_fields = ['answer']

class VoteAdmin(admin.ModelAdmin):
	list_display  = ['question','vote']
	list_filter   = ['question','vote']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Vote,VoteAdmin)


