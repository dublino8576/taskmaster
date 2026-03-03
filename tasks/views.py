from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def task_list(request):
    #this view will display 2 tables, To do and Done, with tasks sorted by due date, with the most recent tasks at the top.
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    context = {
        'to_do_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }

    return render(request, 'tasks/index.html', context)
    