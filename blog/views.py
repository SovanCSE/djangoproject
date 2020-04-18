from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post One',
        'content':'First blog content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Jane done',
        'title':'Blog Post Two',
        'content':'second blog content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})

def about(request):
    return render(request, 'blog/about.html', {'posts':Post.objects.all(),'title':'about'})
