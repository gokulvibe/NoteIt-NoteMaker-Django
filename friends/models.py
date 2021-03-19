from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    userFriend = models.ForeignKey(User, on_delete=models.CASCADE, name="userfriend")
    request_accepted = models.BooleanField(default=False)
    
class Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    opened = models.BooleanField(default=True)