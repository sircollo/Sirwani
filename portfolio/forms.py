from .models import *
from django import forms



class FeedBackForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'name','placeholder': 'Name'}), required=True)
  email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}), required=True)
  message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','name':'message','id':'message','placeholder': 'Message','rows':'4'}), required=True)
  class Meta:
    model = FeedBack
    fields = ('name', 'email','message')