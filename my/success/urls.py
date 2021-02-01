from django.urls import path
from .views import  sucs ,DesiresList, GoalsMy , tasks , task_up



urlpatterns = [
    path('',sucs,name='success' ),
    path('desires',DesiresList.as_view(),name='desires'),
    path('goals',GoalsMy.as_view(),name='goals'),
    #path('tasks',TasksView.as_view(),name='tasks'),
    path('tasks', tasks, name='tasks'),
    path('tasks/<int:pk>', task_up, name='task_up'),
    #path('tasks/<int:pk>', task_up, name='task_del')

]

