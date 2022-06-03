from django.shortcuts import render, redirect
from .models import Tasks

# Create your views here.
def list_tasks(request):
    tasks=Tasks.objects.all()
    return render(request,'list_tasks.html', {"tasks":tasks})

def create_task(request):
    task=Tasks(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task=Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')