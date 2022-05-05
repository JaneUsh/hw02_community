from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LIMITATION = 10


def index(request):
    posts = Post.objects.select_related('group', 'author')[:LIMITATION]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LIMITATION]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)
