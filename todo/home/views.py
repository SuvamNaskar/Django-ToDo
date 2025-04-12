from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout

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

def toggle_status(req, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.status = 0 if task.status == 1 else 1
    task.save()
    return redirect('home')

def login_page(req):
    if req.user.is_authenticated:
        return redirect('home')
    
    if req.method == 'POST':
        data = req.POST
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username=username):
            messages.error(req, 'User not found')
            return render(req, 'login.html', {'error': 'User not found'})
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            messages.info(req, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(req, 'Invalid credentials')
            return render(req, 'login.html', {'error': 'Invalid credentials'})
    
    return render(req, 'login.html')

def register(req):
    if req.user.is_authenticated:
        return redirect('home')
    
    if req.method == 'POST':
        data = req.POST
        username = data.get('username')
        password = data.get('password')
        firstname = data.get('firstname')
        lastname = data.get('lastname')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(req, 'Username already exists')
            return render(req, 'register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username)
        user.set_password(password)
        user.save()
        
        messages.info(req, 'Account Created')
        return redirect('login')
    
    return render(req, 'register.html')

def logout_req(req):
    logout(req)
    messages.info(req, 'Logged out successfully')
    return redirect('home')