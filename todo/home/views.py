from django.shortcuts import render, redirect
from .models import Tasks

def home(req):
    
    if req.method == 'POST':
        data = req.POST
        task = data.get('newTask')

        Tasks.objects.create(
            task = task,
            status = 1
        )
        
    res = Tasks.objects.all()
    context = {
                'page': 'Django ToDo',
                'tasks': res,
              }
    return render(req, 'home.html', context)