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
        
        images = request.FILES.getlist('images')
        print(images)
        print(request.FILES)
        for image in images:
            print("Entered")
            note_image = Image.objects.create(note=note,image=image)
            note_image.save()
        
        images_for_html = Image.objects.filter(note=note)
        return redirect('/editnote/'+str(note.pk))
    
    else:
        return render(request, "mainnotes/addnote.html")
    
def editnote(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        print("Printing title:", title)
        description = request.POST['description']
        if 'hide_note' in request.POST:
            hide_note = True
        else:
            hide_note = False
            
        note = Notes.objects.get(pk=pk)
        note.title = title
        note.description = description
        note.hidden_note = hide_note
        note.save()
        
        return redirect('/editnote/'+str(note.pk))
    
    else:
        note = Notes.objects.get(pk = pk)
        images = Image.objects.filter(note = note)
        return render(request, 'mainnotes/editnote.html', context={'note':note, 'images':images})
