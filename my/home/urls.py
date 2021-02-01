from django.contrib import admin
from django.urls import path, include
from .views import primer , home , register , user_login , user_logout , test

urlpatterns = [
    path('primer/', primer,name='primer'),
    path('', home,name='home'),
    path('register/',register,name='register'),
    path('login/',user_login,name= 'login'),
    path('logout/',user_logout,name= 'logout'),
    path('test/',test,name='test')
]