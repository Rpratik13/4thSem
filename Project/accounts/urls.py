from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('sign-up/', views.sign_up, name='sign-up'),
	path('log-in/', views.log_in, name='log-in'),
	path('log-out/', views.log_out, name='log-out'),
]