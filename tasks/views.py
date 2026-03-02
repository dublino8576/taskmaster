from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def task_list(request):
    #this view will display 2 tables, To do and Done, with tasks sorted by due date, with the most recent tasks at the top.
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'tasks/index.html', {'todo_tasks': todo_tasks, 'done_tasks': done_tasks})


def todo_tasks(request):
    """View for displaying incomplete tasks (to do)"""
    tasks = Task.objects.filter(completed=False).order_by('due_date')
    return render(request, 'tasks/todo.html', {'tasks': tasks})


def done_tasks(request):
    """View for displaying completed tasks (done)"""
    tasks = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'tasks/done.html', {'tasks': tasks})