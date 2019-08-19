from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

class Index(ListView):
    model = Task
    template_name = 'task/index.html'
