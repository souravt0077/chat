from django.db import models
from user.models import User

# Create your models here.

class Rooms(models.Model):
    name=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=250,null=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created']
    
class Message(models.Model):
    body=models.TextField(max_length=1000,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rooms=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

class Doubt(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body=models.TextField(max_length=500,null=True)
    created=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.body[:50]
    
    class Meta:
        ordering=['-created']