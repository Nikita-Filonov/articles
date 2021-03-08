from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response

from .serializer import ArticleSerializer
from blog.models import Article


class ArticleApi(views.APIView):
    def get(self, request):
        articles = Article.objects.all()

        return Response(
            ArticleSerializer(articles, many=True).data
        )

    def post(self, request):
        article = Article.objects.create(
            author=request.data.get('author'),
            title=request.data.get('title'),
            content=request.data.get('content')
        )

        return Response(
            ArticleSerializer(article, many=False).data
        )

    def delete(self, request):
        try:
            Article.objects.get(
                id=request.data.get('id')
            ).delete()
            response = {
                'message': 'Статья была удалена',
                'level': 'success'
            }
        except ObjectDoesNotExist:
            response = {
                "message": 'Такой статьи нет',
                'level': 'danger'
            }

        return Response(response)

    def patch(self, request):
        article = Article.objects.get(
            id=request.data.get('id')
        )
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({
            'message': 'Ошибка обновления статьи',
            'level': 'danger'
        })
