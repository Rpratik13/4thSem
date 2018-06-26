from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={"class":"form-control", "rows": 5, "cols": 20})
        }

