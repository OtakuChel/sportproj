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
        fields = ['date', 'user']

    def __init__(self, *args, **kwargs):
        super(EatingDateForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()  # Скрыть поле выбора пользователя

class EatingForm(forms.ModelForm):
    class Meta:
        model = Eating
        fields = '__all__'
        #exclude = ['date']

    def __init__(self, *args, **kwargs):
        super(EatingForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()  # Скрыть поле выбора пользователя
        self.fields['date'].widget = forms.HiddenInput()  # Скрыть поле выбора пользователя
