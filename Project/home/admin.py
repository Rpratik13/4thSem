from django.contrib import admin
from .models import Question,Answer,QuestionVote,AnswerVote

class QuestionAdmin(admin.ModelAdmin):
	list_display  = ['question','date','tag']
	list_filter   = ['date']
	search_fields = ['question']
	
class AnswerAdmin(admin.ModelAdmin):
	list_display  = ['answer','edit_date']
	list_filter   = ['edit_date']
	search_fields = ['answer']

class QuestionVoteAdmin(admin.ModelAdmin):
	list_display  = ['question','vote']
	list_filter   = ['question','vote']


class AnswerVoteAdmin(admin.ModelAdmin):
	list_display  = ['answer','vote']
	list_filter   = ['answer','vote']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(QuestionVote,QuestionVoteAdmin)
admin.site.register(AnswerVote,AnswerVoteAdmin)

