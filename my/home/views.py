from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

# Create your views here.
def primer(request):
    return render(request, 'primer.html')

def home (request):
    return render(request, 'home.html')




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'You registered :)')
            return redirect('home')
        else :
            messages.error(request,'ooops...somes wrong! :( ')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, f'Hello {user.username} :)')
            return redirect('home')
        else:
            messages.error(request, 'ooops...somes wrong! :( ')
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],form.cleaned_data['content'],from_email='radukartem995@gmail.com',recipient_list=[form.cleaned_data['recipient']],fail_silently=False)
            if mail:
                messages.success(request, ' Message send. :)')
                return redirect('test')
            else:
                messages.error(request, 'error send :( ')
    else:
        form = ContactForm()
    return render(request,'test.html',{'form': form})