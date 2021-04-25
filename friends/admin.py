from django.contrib import admin
from .models import FriendRequest, User
# Register your models here.
admin.site.register(FriendRequest)
admin.site.register(User)