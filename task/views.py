from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

class Index(ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'task'



class DetailView(DetailView):
    model = Task
    template_name = 'task/detail.html'
    context_object_name = 'task'
