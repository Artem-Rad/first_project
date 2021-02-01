from .models import ActionsOfDay
from django import forms

class ActionsForm(forms.ModelForm):
    class Meta:
        model = ActionsOfDay
        fields = ['time','task','comment']
        widgets = {
            'name': forms.TimeInput(attrs={'class':'form-control'}),
            'task': forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.TextInput(attrs={'class':'form-control'}),
                   }


