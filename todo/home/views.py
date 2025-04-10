from django.shortcuts import get_object_or_404, render, redirect
from .models import Tasks

def home(req):
    
    if req.method == 'POST':
        data = req.POST
        task = data.get('newTask')

        Tasks.objects.create(
            task = task,
            status = 0
        )
        
    res = Tasks.objects.all()
    context = {
                'page': 'Django ToDo',
                'tasks': res,
              }
    return render(req, 'home.html', context)

def delete_task(req, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('home')
