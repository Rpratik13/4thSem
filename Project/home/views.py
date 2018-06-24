from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer


class HomeView(TemplateView):
	template_name = 'home/question_list.html'

	def get(self,request):
		form = HomeForm()
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = HomeForm(request.POST)
		return HttpResponse("Works")
		# return render(request, self.template_name,'Works')


def index(request):
    return render(request,"E:/4thSem/Project/templates/navbar.html")

def question_list(request,id=None):
	question_list = Question.objects.all()
	answer_list   = Answer.objects.all()
	content       = {
		"question_list":question_list,
		"answer_list":answer_list
	}

	return render(request,"home/question_list.html",content)

def votes_update(self,request):

	if request.method == 'POST':
		return HttpResponse('Works')	