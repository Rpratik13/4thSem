from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer,QuestionVote,AnswerVote
from django.shortcuts import get_object_or_404,redirect
from .forms import QuestionForm,AnswerForm
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
	question           = Question.objects.filter(id = question_id)
	answers            = AnswerVote.objects.filter()
	answer_upvotes     = answers.filter(vote=1).count()
	answer_downvotes   = answers.filter(vote=-1).count()
	answer_votes = answer_upvotes - answer_downvotes
	
	answer_list        = Answer.objects.filter(question_id = question_id)
	question_upvotes   = QuestionVote.objects.filter(question_id=question_id,vote=1).count()
	question_downvotes = QuestionVote.objects.filter(question_id=question_id,vote=-1).count()
	question_votes     = question_upvotes - question_downvotes
	if request.method == "POST":
		form = AnswerForm(request.POST)
		new_answer = form.save(commit=False)
		new_answer.date = datetime.datetime.now()
		new_answer.question_id = question_id
		new_answer.save()
		return self
	else:
		form = AnswerForm()
		context = {
		"question" : question,
		"answer_list" : answer_list,
		"question_votes" : question_votes,
		'form': form,
		}
		return render(request, 'home/question_detail.html', context)
  
# def answer_detail(request,question_id,answer_id):
	
def question_upvote(request,question_id):
	question = Question.objects.filter(id=question_id)
	votes    = QuestionVote.objects.filter(question_id=question_id)
	new_vote = QuestionVote(question_id=question_id,vote=1)
	
	if votes.filter(question_id = question_id,vote=1).exists():
		votes.delete()
	elif votes.filter(question_id=question_id,vote=-1):
		QuestionVote.objects.filter(question_id=question_id,vote=-1).delete()
		new_vote.save()	
	else:
		new_vote.save()	
	return redirect('question_detail', question_id=question_id)

def question_downvote(request,question_id):
	question = Question.objects.filter(id=question_id)
	votes    = QuestionVote.objects.filter(question_id=question_id)
	new_vote = QuestionVote(question_id=question_id,vote=-1)
	
	if votes.filter(question_id = question_id,vote=-1).exists():
		votes.delete()
	elif votes.filter(question_id=question_id,vote=1):
		QuestionVote.objects.filter(question_id=question_id,vote=1).delete()
		new_vote.save()	
	else:
		new_vote.save()	
	return redirect('question_detail', question_id=question_id)

def answer_upvote(request,answer_id,question_id):
	answer = Answer.objects.filter(id=answer_id)
	votes    = AnswerVote.objects.filter(answer_id=answer_id)
	new_vote = AnswerVote(answer_id=answer_id,vote=1)
	
	if votes.filter(answer_id = answer_id,vote=1).exists():
		votes.delete()
	elif votes.filter(answer_id=answer_id,vote=-1):
		AnswerVote.objects.filter(answer_id=answer_id,vote=-1).delete()
		new_vote.save()	
	else:
		new_vote.save()	
	return redirect('question_detail', question_id=question_id)

def answer_downvote(request,answer_id,question_id):
	answer = Answer.objects.filter(id=answer_id)
	votes    = AnswerVote.objects.filter(answer_id=answer_id)
	new_vote = AnswerVote(answer_id=answer_id,vote=-1)
	
	if votes.filter(answer_id = answer_id,vote=-1).exists():
		votes.delete()
	elif votes.filter(answer_id=answer_id,vote=1):
		AnswerVote.objects.filter(answer_id=answer_id,vote=1).delete()
		new_vote.save()	
	else:
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

def tag_filter(request,tag):
	question_list = Question.objects.filter(tag=tag)
	answer_list   = Answer.objects.filter()
	content       = {
		"question_list":question_list,
		"answer_list":answer_list
	}

	return render(request,"home/question_list.html",content)

	