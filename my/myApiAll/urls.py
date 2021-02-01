from django.urls import path
from .views import index, UsersListSerializer, UserViewSerializer

urlpatterns = [
    path('',index,name='API'),
    path('get_users',UsersListSerializer.as_view(),name='get_users'),
    path('get_users/<int:pk>',UserViewSerializer.as_view(),name='get_user')
]

