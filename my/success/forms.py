from .models import Task
from django import forms

class GoalsForm(forms.Form):
    context = forms.CharField(max_length=100,label='Твои цели',widget=forms.TextInput(attrs={'class': 'form-control'}))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'priority', 'kind']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'kind': forms.Select(attrs={'class': 'form-control'}),
        }

