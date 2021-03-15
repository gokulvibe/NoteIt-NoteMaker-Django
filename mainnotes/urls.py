from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainnotes, name='mainnotes'),
    path('addnote', views.addNote, name='addnote'),
    path('editnote/<int:pk>/', views.editnote, name='editnote'),
    path('trashnote/<int:pk>/', views.trashnote, name='trashnote'),
    path('hidenote/<int:pk>/', views.hidenote, name='hidenote'),
    path('hiddennotes', views.hidden_notes, name='hiddennotes'),
    path('trashednotes', views.trashed_notes, name='trashdnotes'),
    path('emptytrash', views.empty_trash, name='empty_trash'),
    path('addhiddennote', views.addHiddenNote, name='addhiddennote'),
]