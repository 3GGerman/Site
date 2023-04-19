# Generated by Django 4.1.7 on 2023-04-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movies_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Фильмы', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.RemoveField(
            model_name='movies',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='movies',
            name='date_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
