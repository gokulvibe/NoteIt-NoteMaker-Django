from django.urls import path
from . import views

urlpatterns = [
    path('addfriend', views.send_friend_request, name='addfriend'),
    # path('friendrequests', views.viewfriends, name='viewfriends'),
]