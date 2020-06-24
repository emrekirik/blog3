from django.shortcuts import render
from .models import Post,About
from django.utils import timezone


def index(request):
    post = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    context = {
        'post' : post
    }
    return render(request, 'home/index.html', context)


def about(request):
    hakkimda = About.objects.get(id=1)
    context = {
        'hakkimda' : hakkimda
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post' : post,
    }
    return render(request, 'home/detail.html' , context,)