from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.core.paginator import Paginator
from .forms import PostForm


LIMITATION = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_author = author.posts.all()
    paginator = Paginator(post_author, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    # Здесь код запроса к модели и создание словаря контекста

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    count_posts = post.author.posts.count()
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'post': post,
        'count_posts': count_posts,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            breakpoint()
            group = Group.objects.get(id=form.data['group'])
            post = Post(
                group=group,
                text=form.data['text']
            )
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user.username)

    form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})
