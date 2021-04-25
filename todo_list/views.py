from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            list = List.objects.all
            context = {
                'list': list
                }
            messages.success(request, 'item has been added successfully')
            return render(request, 'pages/index.html', context)
    else:
        list = List.objects.all
        context = {
            'list': list
            }
        return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'item has been deleted successfully')
    return redirect('index')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')

def edit(request, list_id):
    if request.method == 'POST':
        list = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=list)

        if form.is_valid():
            form.save()
            messages.success(request, 'item has been edited successfully')
            return redirect('index')
    else:
        list = List.objects.get(pk=list_id) 
        context = {
            'list': list
            }
        return render(request, 'pages/edit.html', context)