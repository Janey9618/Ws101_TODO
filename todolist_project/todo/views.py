from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')