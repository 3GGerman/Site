# Generated by Django 4.1.7 on 2023-04-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movies_options_movies_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='name',
            new_name='title',
        ),
    ]