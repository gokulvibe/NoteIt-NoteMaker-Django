from django.shortcuts import render

# Create your views here.


def mainnotes(request):
    return render(request, 'mainnotes/mainnotes.html')