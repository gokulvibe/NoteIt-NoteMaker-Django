from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainnotes, name='mainnotes'),
    path('addnote', views.addNote, name='addnote'),
    path('editnote/<int:pk>/', views.editnote, name='editnote'),
]