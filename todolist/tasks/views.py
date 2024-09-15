from django.shortcuts import render

# Create your views here.

def task_view(request):
    return render(request, 'tasks/tasks.html')