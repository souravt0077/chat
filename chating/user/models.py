from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    img=models.ImageField(default='user.png',null=True)
    
    def __str__(self):
        return self.username

    class Meta:
        ordering=['-date_joined']

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
