from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def task_view(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Task.objects.create(name=name, description=description)
        return redirect('tasks')
    
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def completed(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/completed_tasks.html', {
        'tasks': tasks,
    })

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.mark_completed()
    return redirect('tasks')
