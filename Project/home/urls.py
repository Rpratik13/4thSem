from . import views
from django.urls import path

urlpatterns = [
   	#path('',views.index),
    path('',views.question_list),
]
