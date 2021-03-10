# Generated by Django 3.1.7 on 2021-03-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сатьи')),
                ('content', models.TextField(verbose_name='Текст статьи')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
            ],
        ),
    ]