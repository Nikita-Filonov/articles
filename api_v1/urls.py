from django.urls import path
from .views import ArticleApi

urlpatterns = [
    path('article/', ArticleApi.as_view(), name='article_api')
]
