from . import views
from django.urls import path

urlpatterns = [
   	#path('',views.index),
    path('',views.question_list,name='question_list'),
    path('question/<int:question_id>',views.question_detail, name='question_detail'),
    path('question/<int:question_id>/upvote',views.question_upvote, name='question_upvote'),
    path('question/<int:question_id>/downvote',views.question_downvote, name='question_downvote'),
    path('question/<int:question_id>/answer_upvote/<int:answer_id>',views.answer_upvote, name='answer_upvote'),
    path('question/<int:question_id>/answer_downvote/<int:answer_id>',views.answer_downvote, name='answer_downvote'),
    path('question/add',views.add_question, name='add_question'),
 	path('question/tag/<str:tag>',views.tag_filter, name='tag_filter'), 
]
