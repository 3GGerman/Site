# Generated by Django 4.1.7 on 2023-04-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movies_options_remove_movies_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['date_create'], 'verbose_name': 'Фильмы', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AddField(
            model_name='movies',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
