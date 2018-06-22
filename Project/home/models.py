from django.db import models


class Question(models.Model):
	question = models.CharField(max_length=100)
	date     = models.DateTimeField()
	
	def __str__(self):
		return self.question

class Answer(models.Model):
	question  = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer    = models.TextField()
	edit_date = models.DateTimeField()


	def __str__(self):
		return self.answer