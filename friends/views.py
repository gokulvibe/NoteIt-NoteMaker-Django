from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import FriendRequest, User
from django.contrib import messages
# Create your views here.
    
    
def send_friend_request(request):
    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.get(pk = request.POST['friend'])
        friend_request, created = FriendRequest.objects.get_or_create(from_user = from_user, to_user = to_user)
        
        if created:
            messages.info(request, 'Request has been sent')
            return redirect('/addfriend')
        
        else:
            messages.info(request, 'Request has been already sent')
            return redirect('/addfriend')
        
    else:
        try:
            searchable = request.GET['search']
        except:
            searchable = ''
            
        all_users_searched = User.objects.filter(email__contains = searchable).exclude(pk=request.user.pk)
        friends = request.user.friends
        
        return render(request, 'friends/addfriend.html',
                      context={'all_users_searched' : all_users_searched, 'friends' : friends})
        