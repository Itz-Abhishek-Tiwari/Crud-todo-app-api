# Generated by Django 5.0.7 on 2024-07-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
    ]
