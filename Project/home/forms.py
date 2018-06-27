from django import forms
from .models import Question,Answer


class QuestionForm(forms.ModelForm):
    TAG_CHOICE = [
    ('engineering','Engineering'),
    ('science','Science'),
    ]
    tag= forms.CharField(widget=forms.Select(choices=TAG_CHOICE))
    class Meta:
        model = Question
        fields = ['question','tag']
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
