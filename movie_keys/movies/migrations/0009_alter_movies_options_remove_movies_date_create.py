# Generated by Django 4.1.7 on 2023-04-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movies_date_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['id', 'title'], 'verbose_name': 'Фильмы', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.RemoveField(
            model_name='movies',
            name='date_create',
        ),
    ]
