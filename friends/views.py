from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import FriendRequest, User
from django.contrib import messages
from django.http import HttpResponse
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
        
        
def display_friend_requests(request):
    friend_requests = FriendRequest.objects.filter(to_user = request.user)
    
    return render(request, 'friends/friend_requests.html', context = {'friend_requests' : friend_requests})
        
def accept_request(request):
    if request.method == 'POST':
        friend_request = FriendRequest.objects.get(id = request.POST['friend'])
        
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        
        friend_request.delete()
        
        messages.info(request, 'Friend request accepted')
        return redirect('/display_friend_requests')
    
    else:
        return HttpResponse("Something's fishy bruh!")
    
def delete_request(request):
    friend_request = FriendRequest.objects.get(id = request.POST['friend'])
    friend_request.delete()
        
    messages.info(request, 'Friend request deleted')
    return redirect('/display_friend_requests')
    
    
def remove_friend(request):
    if request.method == 'POST':
        
        friend = User.objects.get(pk = request.POST['friend'])
        request.user.friends.remove(friend)
        
        messages.info(request, 'Friend request deleted')
        return redirect('/addfriend')
    
    else:
        return HttpResponse("Something's fishy bruh!")
    
def view_friends(request):
    
    try:
        searchable = request.GET['search']
    except:
        searchable = ''
            
    user = request.user
    all_friends_searched = user.friends.all()
    
    return render(request, 'friends/viewfriends.html',
                    context={'all_friends_searched' : all_friends_searched})
