from django.urls import path
from .views import timetable , add_task , task_update , task_del


urlpatterns = [
    path('',timetable,name='timetable'),
    path('add/<int:day_id>',add_task,name='add_task'),
    path('up/<int:task_id>',task_update,name='up_task'),
    path('del/<int:task_id>',task_del,name='del_task')
    #path('add',add_task,name='add_task')
]