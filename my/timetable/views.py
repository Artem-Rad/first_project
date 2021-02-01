from django.shortcuts import render, redirect
from .models import ActionsOfDay, Days
from .forms import ActionsForm
from django.contrib import messages


def timetable(request):
    days=Days.objects.all()
    task = ActionsOfDay.objects.filter(user_id=request.user.id)
    con = {
         'days': days,
         'task': task,
    }
    return render(request, 'timetable.html', con)

def add_task(request,day_id):
    day = Days.objects.get(pk=day_id)
    if request.method == "POST":
        form = ActionsForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            ActionsOfDay.objects.create(
                time = data['time'],
                task = data['task'],
                comment = data['comment'],
                day_id = day_id,
                user_id = request.user.id
            )
            messages.success(request, 'task added')
            return redirect('timetable')
        else :
            messages.error(request, 'oops')
    else:
        form = ActionsForm()
    cont = {
        'form':form,
        'day': day
    }
    return render(request,'add_task.html',cont)

def task_update(request,task_id):
    if request.method =='POST':
        form = ActionsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            act = ActionsOfDay.objects.get(id=task_id)
            act.time = data['time']
            act.task = data['task']
            act.comment = data['comment']
            act.save()
            messages.success(request, 'task updated')
            return redirect('timetable')
    else :
        form = ActionsForm()
    task = ActionsOfDay.objects.get(id=task_id)
    con = {
        'form':form,
        'task':task
    }
    return render(request, 'up_task.html',con)


def task_del(request, task_id):
    task = ActionsOfDay.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'task delete')
    return redirect('timetable')