# Generated by Django 4.1 on 2024-05-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_task_post_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='task_time',
            field=models.CharField(default='', max_length=200),
        ),
    ]
