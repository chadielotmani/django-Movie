# Generated by Django 4.2.7 on 2023-11-28 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yeet', '0003_remove_movie_genres_delete_genre_movie_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
    ]
