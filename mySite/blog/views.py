from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def contact(request):
    return render(request, "blog/contact.html")

def about(request):
    return render(request, "blog/about.html")

def login(request):
    return render(request, "blog/login.html")