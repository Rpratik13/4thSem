from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer

def index(request):
    return render(request,"navbar.html",{})

def question_list(request,id=None):
	question_list = Question.objects.all()
	content = {
		"question_list":question_list
	}

	return render(request,"question_list.html",content)