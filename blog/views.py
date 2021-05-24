from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all().order_by("-id")[:3]
    return render(request, 'blog/index.html', {'posts': posts})


def blogList(request):
    AllPosts = Post.objects.all()
    return render(request, 'blog/blog-list.html', {'AllPosts': AllPosts})
