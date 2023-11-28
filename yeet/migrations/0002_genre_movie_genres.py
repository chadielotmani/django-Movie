# Generated by Django 4.2.7 on 2023-11-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='yeet.genre'),
        ),
    ]