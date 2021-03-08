from django.shortcuts import render, redirect
from .models import Notes, Image
from django.contrib.auth.decorators import login_required
# Create your views here.


def mainnotes(request):
    if request.user.is_authenticated:
        allNotes = Notes.objects.filter(owner = request.user)
        return render(request, 'mainnotes/mainnotes.html', context = {'all_notes': allNotes})
    else:
        return redirect('login')
    
@login_required(redirect_field_name='login')
def addNote(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        print("Printing title:",title)
        owner = request.user
        
        if 'hide_note' in request.POST:
            hide_note = True
        else:
            hide_note = False
        
        print("Printing Hide:", hide_note)
        note = Notes(owner=owner, title=title, description=description, hidden_note = hide_note)
        note.save()
        
        return render(request, 'mainnotes/editnote.html', context={'note':note})
    
    else:
        return render(request, "mainnotes/addnote.html")