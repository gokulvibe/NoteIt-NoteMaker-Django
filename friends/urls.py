from django.urls import path
from . import views

urlpatterns = [
    path('addfriend', views.send_friend_request, name='addfriend'),
    # path('friendrequests', views.viewfriends, name='viewfriends'),
    path('display_friend_requests', views.display_friend_requests, name='display_friend_requests'),
    path('acceptrequest', views.accept_request, name='accept_request'),
    path('deleterequest', views.delete_request, name='delete_request'),
    path('removefriend', views.remove_friend, name='remove_friend'),
    path('viewfriends', views.view_friends, name='view_friends'),
]