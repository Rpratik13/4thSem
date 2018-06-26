from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer,Vote
from django.shortcuts import get_object_or_404,redirect
from .forms import QuestionForm
import datetime


# class HomeView(TemplateView):
# 	template_name = 'home/question_list.html'

# 	def get(self,request):
# 		form = HomeForm()
# 		return render(request, self.template_name,{'form':form})

# 	def post(self,request):
# 		form = HomeForm(request.POST)
# 		return HttpResponse("Works")
# 		# return render(request, self.template_name,'Works')


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

def question_detail(request, question_id):
	question    = Question.objects.filter(id = question_id)
	answer_list = Answer.objects.filter(question_id = question_id)
	content     = {
	"question" : question,
	"answer_list" : answer_list,
	}
	return render(request, "home/question_detail.html", content)
    
def upvote(request,question_id):
	question = Question.objects.filter(id=question_id)
	new_vote = Vote(question_id=question_id,vote=1)
	new_vote.save()	
	return redirect('question_detail', question_id=question_id)

def downvote(request,question_id):
	question = Question.objects.filter(id=question_id)
	new_vote = Vote(question_id=question_id,vote=-1)
	new_vote.save()	
	return redirect('question_detail', question_id=question_id)

def add_question(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		new_question = form.save(commit=False)
		new_question.date = datetime.datetime.now()
		new_question.save()
		return redirect('question_list')
	else:
		form = QuestionForm()
		context = {'form': form}
		return render(request, 'home/add_question.html', context)