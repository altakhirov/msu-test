# Generated by Django 3.2.8 on 2021-10-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20211010_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Файл'),
        ),
    ]