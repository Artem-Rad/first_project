from django.urls import path, include
from .views import temp , city_del



urlpatterns = [
    path('', temp, name='weather'),
    path('del/<int:pk>', city_del, name='city_del')
]