from django.shortcuts import render, redirect
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