from django import forms
from .models import BodySize

#class FeedbackForm(forms.Form):
#    name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#    "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
#    "min_length": "Слишком мало символов, должно быть %(limit_value)d, сейчас символов  %(show_value)d.",
#    "required": "Обязательно к заполнению",
#    })
#    surname = forms.CharField()
#    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#    rating = forms.IntegerField(max_value=100, min_value=0)

class BodySizeForm(forms.ModelForm):
    date = forms.DateField(label='Дата', widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type': 'date'
        }))
    class Meta:
        model = BodySize
        fields = '__all__'
        #labels = {
        #    'name': 'Имя',
        #    'surname': 'Фамилия',
        #    'feedback': 'Отзыв',
        #    'rating': 'Рейтинг',
        #}
        #error_messages = {
        #    'name' : { 'max_length':'ой как много символов',
        #               'min_length': 'ой как мало символов',
        #               'required':'Не должно быть пустым'
        #             },
        #    'surname': {'max_length': 'ой как много символов',
        #             'min_length': 'ой как мало символов',
        #             'required': 'Не должно быть пустым'
        #             },
        #    'feedback': {'max_length': 'ой как много символов',
        #             'min_length': 'ой как мало символов',
        #             'required': 'Не должно быть пустым'
        #             }
        #}