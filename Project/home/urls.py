from . import views
from django.urls import path

urlpatterns = [
   	#path('',views.index),
    path('',views.question_list,name='question_list'),
    path('question/<int:question_id>',views.question_detail, name='question_detail'),
    path('question/<int:question_id>/upvote',views.upvote, name='upvote'),
    path('question/<int:question_id>/downvote',views.downvote, name='downvote'),
    path('question/add',views.add_question, name='add_question'),
    
]
