from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название сатьи',
        null=False
    )

    content = models.TextField(
        verbose_name='Текст статьи',
        null=False
    )

    author = models.CharField(
        max_length=100,
        verbose_name='Автор',
        null=False
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(
        verbose_name='Автор комментария',
        max_length=50,
        null=False
    )
    post_date = models.DateField(
        verbose_name='Дата оставления комментария',
        auto_now=True
    )
    related_article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name='Статья для которой оставлен комментарий',
    )
    comment_text = models.TextField(
        verbose_name='Текст комментария',
        null=False,
        default=''
    )

    def __str__(self):
        return self.author
