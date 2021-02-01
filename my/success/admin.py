from django.contrib import admin
from .models import Desires, KindTask, PriorityTask, Task
# Register your models here.

admin.site.register(Desires)
admin.site.register(KindTask)
admin.site.register(PriorityTask)
admin.site.register(Task)