from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Days(models.Model):
    name = models.CharField('День недели',max_length=10)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

class ActionsOfDay(models.Model):
    time = models.TimeField('Время')
    task = models.CharField('Чем будешь заниматься',max_length=100)
    comment = models.CharField('Комментарий', max_length=100, blank=True,null=True)
    day = models.ForeignKey(Days,verbose_name='день недели', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,verbose_name='Кто автор', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'В {self.time} : {self.task}  ({self.comment})'

    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'

