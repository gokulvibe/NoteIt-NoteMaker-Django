from django.urls import path
from . import views

urlpatterns = [
    path('addfriend', views.addfriend, name='addfriend'),
    path('viewfriends', views.viewfriends, name='viewfriends'),
]