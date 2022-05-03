from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LIMITATION_OUTPUT = 10

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:LIMITATION_OUTPUT]
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LIMITATION_OUTPUT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)