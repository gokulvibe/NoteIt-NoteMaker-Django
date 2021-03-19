from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Friend, Notification
# Create your views here.

def addfriend(request):
    if request.method=="POST":
        friend_id = request.POST['friend']
        friend = User.objects.get(pk = friend_id)
        friend_object = Friend(user=request.user, userFriend = friend)
        friend_object.save()
    try:
        searchable = request.GET['search']
    except:
        searchable = ''
        
    user_results = User.objects.filter(email__contains = searchable)
    
    return render(request, 'friends/addfriend.html', context={'user_results': user_results})

def viewfriends(request):
    pass
    