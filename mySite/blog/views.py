from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import random

colors = ['red', 'yellow', 'blue', 'purple']
color = random.choice(colors)


def home(request):
    context = {
        'posts': Post.objects.all(),
        'color': color
    }
    return render(request, "blog/home.html", context)

def contact(request):
    return render(request, "blog/contact.html")

def about(request):
    return render(request, "blog/about.html")

def login(request):
    return render(request, "blog/login.html")

def test(request):
    return render(request, "blog/test.html")