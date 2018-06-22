from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer

def index(request):
    return render(request,"navbar.html",{})

def question_list(request,id=None):
	question_list = Question.objects.all()
	answer_list   = Answer.objects.all()
	content       = {
		"question_list":question_list,
		"answer_list":answer_list
	}


	return render(request,"home/question_list.html",content)