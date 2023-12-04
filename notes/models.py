from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=30)
    note_body = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    ref_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

