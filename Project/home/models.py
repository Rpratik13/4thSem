from django.db import models


class Question(models.Model):
	question = models.CharField(max_length = 100)
	date     = models.DateTimeField()
	tag      = models.CharField(max_length=20)
	
	def __str__(self):
		return self.question

class Answer(models.Model):
	question  = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer    = models.TextField()
	edit_date = models.DateTimeField()

	def __str__(self):
		return self.answer

class QuestionVote(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	vote     = models.IntegerField(default=0)

class AnswerVote(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	vote   = models.IntegerField(default=0)
	
	def get_results_dict(self,answer_id):
		res = []
		for choice in self.choice_set.all():
			d = {}
			answer_upvotes = choice.vote.filter(answer_id=answer_id,vote=1).count()
			answer_downvotes = choice.vote.filter(answer_id=answer_id,vote=1).count()
			votes = answer_upvotes - answer_downvotes
			d['votes'] = votes
			res.append(d)
		return res
