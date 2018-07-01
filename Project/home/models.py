from django.db import models


class Question(models.Model):
	question = models.CharField(max_length = 100)
	date     = models.DateTimeField()
	tag      = models.CharField(max_length=20)
	votes    = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.question

class Answer(models.Model):
	question  = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer    = models.TextField()
	edit_date = models.DateTimeField()
	votes     = models.IntegerField(default = 0)

	def __str__(self):
		return self.answer

class QuestionVote(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	vote     = models.IntegerField(default=0)

class AnswerVote(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	vote   = models.IntegerField(default=0)
	
