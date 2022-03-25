
from django.core import validators
from django import forms
from .models import contact

class contact_me(forms.ModelForm):
    class Meta:
      model = contact
      fields=['Name','Email_Address','Text']
      labels = {'Name':'Enter Name','Email_Address':'Enter Email','Text':'Enter text'}

