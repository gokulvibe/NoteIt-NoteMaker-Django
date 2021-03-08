from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    recently_modified_date = models.DateTimeField(auto_now=True)
    hidden_note = models.BooleanField(default=False)
    trashed_note = models.BooleanField(default=False)
    
    def excerpt(self):
        if len(self.description) <= 60:
            return self.description
        else:
            return (self.description[0:60] + "...")
    
class Image(models.Model):
    image = models.ImageField(upload_to='notesImages/')
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)