from django.urls import path

from .views import article_list, view_article, create_article, login_view, register_view, logout_view
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('regitration/', register_view, name='registration'),
    path('list/', login_required(article_list, login_url='blog:login'), name='list'),
    path('create-article/', login_required(create_article, login_url='blog:login'), name='create_article'),
    path('view/<int:article_id>/', login_required(view_article, login_url='blog:login'), name='view')
]
