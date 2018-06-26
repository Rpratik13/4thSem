from django import forms
from .models import Question,Answer


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={"class":"form-control", "rows": 5, "cols": 20})
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={"class":"form-control", "rows": 5, "cols": 20})
        }
