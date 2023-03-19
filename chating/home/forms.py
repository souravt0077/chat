from django.forms import ModelForm
from .models import Rooms,Message
from django import forms

class RoomForm(ModelForm):
    name= forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'placeholder':'Room Name','class':'form-control'}))
    password= forms.CharField(label='',max_length=255,widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control'}))
    class Meta:
        model=Rooms
        fields=['name']
    
    def __init__(self, *args, **kwargs):
        super(RoomForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Room Name'
        self.fields['name'].widget.attrs['class']='form-control'

        self.fields['password'].widget.attrs['placeholder']='password'
        self.fields['password'].widget.attrs['class']='form-control'

class MessageForm(ModelForm):
    body= forms.CharField(label='',max_length=1000,widget=forms.TextInput(attrs={'placeholder':'Type here....','class':'form-control'}))
    class Meta:
        model=Message
        fields='__all__'
        exclude=['user','rooms']
    
    def __init__(self, *args, **kwargs):
        super(MessageForm,self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder']='Type here...'
        self.fields['body'].widget.attrs['class']='form-control'


