from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class userForm(UserCreationForm):
    username= forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    email= forms.EmailField(label='',max_length=255,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}))
    # img=forms.ImageField(label='',widget=forms.(attrs={'placeholder':'profile picture','class':'form-control'}))
    password1= forms.CharField(label='',max_length=255,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    password2= forms.CharField(label='',max_length=255,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','img','password1','password2']
    
    def __init__(self, *args,**kwargs):
        super(userForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].widget.attrs['class']='form-control'

        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['email'].widget.attrs['class']='form-control'

        # self.fields['img'].widget.attrs['placeholder']='image'
        # self.fields['img'].widget.attrs['class']='form-control'

        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].widget.attrs['class']='form-control'
        
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].widget.attrs['class']='form-control'

   