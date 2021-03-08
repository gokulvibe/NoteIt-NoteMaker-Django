from django.shortcuts import render, redirect
from .models import Notes, Image
# Create your views here.


def mainnotes(request):
    if request.user.is_authenticated:
        allNotes = Notes.objects.filter(owner = request.user)
        return render(request, 'mainnotes/mainnotes.html', context = {'all_notes': allNotes})
    else:
        return redirect('login')
    
    
def addNote(request):
    pass