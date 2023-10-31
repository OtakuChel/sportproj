from django import forms
from .models import EatingDate, Eating

class EatingDateForm(forms.ModelForm):
    date = forms.DateField(label='Дата', widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type': 'date'
        }))
    class Meta:
        model = EatingDate
        fields = ['date']

class EatingForm(forms.ModelForm):
    class Meta:
        model = Eating
        fields = '__all__'
        #exclude = ['date']

