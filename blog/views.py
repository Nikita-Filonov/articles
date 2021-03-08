from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib.auth.models import User


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:list')
        else:
            messages.info(request, 'Имя пользователя или пароль не верные')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password1']
        )

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('blog:login')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {
        'articles': articles,
        'user': request.user
    })


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        Comment.objects.create(
            author=request.POST['author'],
            comment_text=request.POST['comment_text'],
            related_article=article
        )

    comments = Comment.objects.filter(related_article=article).order_by('-id')

    return render(request, 'view_article.html', {
        'article': article,
        'comments': comments
    })


def create_article(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.POST['author']
        )
        return redirect('blog:list')

    return render(request, 'create_article.html')
