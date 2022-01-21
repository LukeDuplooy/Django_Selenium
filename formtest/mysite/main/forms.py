from django import forms
from .models import Car

class CarForm(forms.ModelForm):

  class Meta:
    model = Car
    fields = ('name','year','hp','top_speed_mph','weight_kg')