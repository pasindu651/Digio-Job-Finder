from cProfile import label
from socket import fromshare
from django import forms
from django.forms import ModelForm

from .models import *


class ApplicantForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    class Meta:
        model = Applicant
        fields = '__all__'
        