from django.urls import path
from .views import index, UsersListSerializer, UserViewSerializer #, DesiresListView , DesireView    #DesireView , DesiresView ,  #, get_desires , get_desire



urlpatterns = [
    #path('get_desire',get_desires,name='get_desires'),
    #path('get_desire/<int:des_pk>',get_desire,name='get_desire')
    path('',index,name='API'),
    path('get_users',UsersListSerializer.as_view(),name='get_users'),
    path('get_users/<int:pk>',UserViewSerializer.as_view(),name='get_user')
]

