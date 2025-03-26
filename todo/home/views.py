from django.shortcuts import render

def home(req):
    context = {
                'page': 'Django ToDo',
              }
    return render(req, 'home.html', context)