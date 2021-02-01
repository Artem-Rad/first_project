from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Desires, Task, Goals
from .forms import TaskForm
from django.views import View
from django.contrib import messages



class DesiresList(ListView):
    model = Desires
    template_name = 'success/desires.html'
    context_object_name = 'desires'


class GoalsMy(View):
    template_name = 'success/goals.html'

    def get(self, request):
        goals = Goals.objects.filter(user_id=request.user.id)
        con = {
            'goals': goals
        }
        return render(request, self.template_name, con)


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(
                text=data['text'],
                priority=data['priority'],
                kind=data['kind'],
                user_id=request.user
            )
            messages.success(request, 'task added')
            return redirect('success')
        else:
            messages.error(request, 'oops')

    urgent_work_tasks = Task.objects.filter(user_id=request.user.id, kind_id=2, priority_id=1)
    n_urgent_work_tasks = Task.objects.filter(user_id=request.user.id, kind_id=2, priority_id=2)
    n_important_work_tasks = Task.objects.filter(user_id=request.user.id, kind_id=2, priority_id=3)
    urgent_personal_tasks = Task.objects.filter(user_id=request.user.id, kind_id=1, priority_id=1)
    n_urgent_personal_tasks = Task.objects.filter(user_id=request.user.id, kind_id=1, priority_id=2)
    n_important_personal_tasks = Task.objects.filter(user_id=request.user.id, kind_id=1, priority_id=3)
    form = form = TaskForm()
    con = {
    'uwt': urgent_work_tasks,
    'nuwt':n_urgent_work_tasks,
    'niwt': n_important_work_tasks,
    'upt': urgent_personal_tasks,
    'nupt': n_urgent_personal_tasks,
    'nipt':n_important_personal_tasks,
    'form': form
    }
    return render(request, 'success/tasks.html', con)


def task_up(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.text = data['text']
            task.priority = data['priority']
            task.kind = data['kind']
            task.save()
            messages.success(request, 'task updated')
            return redirect('timetable')
    else:
        form = TaskForm()
    con = {
        'form': form,
        'task': task
    }
    return render(request, 'success/taskupdate.html', con)



def sucs(request):
    return render(request,'success/success.html')
