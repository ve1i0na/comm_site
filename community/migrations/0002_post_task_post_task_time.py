# Generated by Django 4.1 on 2024-05-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='task',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='task_time',
            field=models.IntegerField(default=0),
        ),
    ]
