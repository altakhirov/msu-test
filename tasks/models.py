from django.db import models


class Task(models.Model):
    created_by = models.ForeignKey('users.User', verbose_name='Создатель', on_delete=models.CASCADE)
    responsibles = models.ManyToManyField('users.User', verbose_name='Исполнители', related_name='responsibles')
    title = models.CharField(max_length=1024, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    deadline = models.DateField(verbose_name='Дата завершения задачи')
    file = models.FileField(blank=True, verbose_name='Файл', upload_to='task-files/')

    def __str__(self):
        return self.title
