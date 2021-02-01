from django.db import models
from django.contrib.auth.models import User

class Desires(models.Model):
    contect = models.TextField(max_length=300)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} хочу {self.contect}'

class Goals(models.Model):
    context = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    create_at = models.DateField(auto_now_add=True)


class PriorityTask(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}  tasks {self.pk}'

class KindTask(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}  tasks'


class Task(models.Model):
    text = models.CharField(max_length=10)
    priority = models.ForeignKey(PriorityTask,on_delete=models.PROTECT,verbose_name='priority')
    kind = models.ForeignKey(KindTask,on_delete=models.PROTECT,verbose_name='kind')
    is_do = models.BooleanField(default=False,verbose_name='have done?')
    user_id = models.ForeignKey(User,verbose_name='Кто автор', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.text}'
