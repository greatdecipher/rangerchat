from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    # room name, no need ID, django already have
    name = models.CharField(max_length=1000)

class Message(models.Model):
    #the message itself
    value = models.CharField(max_length=1000000)
    #date of the message
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    # which room this message being sent to.
    room = models.CharField(max_length=1000000)
