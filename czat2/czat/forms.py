from django.forms import ModelForm, TextInput
from czat.models import Wiadomosc
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EdytujWiadomoscForm(ModelForm):
	class Meta:
		model = Wiadomosc
		fields = ['tekst', 'data_pub']
		exclude = ['autor']
		widgets = {'tekst': TextInput(attrs={'size' : 60})}



