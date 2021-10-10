# Generated by Django 3.2.8 on 2021-10-09 21:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='responsibles',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Исполнители'),
        ),
    ]
