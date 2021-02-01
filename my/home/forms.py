from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='tema',widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(max_length=100, label='text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows':5}))
    recipient = forms.CharField(max_length=100, label='recipient', widget=forms.EmailInput(attrs={'class':'form-control'}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,label='Login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,label='Login',help_text='-user name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=100,label='Repeat password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')


