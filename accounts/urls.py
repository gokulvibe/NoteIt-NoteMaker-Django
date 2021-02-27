from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('notes',views.notes, name='notes'),
    path('logout',views.logout,name='logout'),
]