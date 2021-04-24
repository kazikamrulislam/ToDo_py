from django.shortcuts import render
from .models import List

def index(request):
    
    list = List.objects.all

    context = {
        'list': list
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')