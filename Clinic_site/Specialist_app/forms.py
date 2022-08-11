from .models import Appointment, Comments
from django import forms
from django.forms import ModelForm, TimeInput, TextInput, Select, SelectDateWidget
from django.utils.translation import gettext_lazy

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['specialist', 'cabinet', 'date', 'timeslot', 'patient_name', 'patient_last_name']

        widgets = {
            'specialist': Select(attrs={
                'class': 'form-control',
                'placeholder': "Вибір спеціаліста"
            }),

            'cabinet': Select(attrs={
                'class' : 'form-control',
                'placeholder': 'Вибір кабінету'

            }),

            'date': SelectDateWidget(attrs={
                'class': '',
                'placeholder': 'Дата'
            }),

            'time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Час',
                'style': 'width:80%;'
            }),

            'patient_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': gettext_lazy('Ім`я')
            }),

            'patient_last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': gettext_lazy('Прізвище')
            })
        }

class CommentsForm(ModelForm):
    comment = forms.CharField(label='Коментар', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%;'}))
    class Meta:
        model = Comments
        fields = ['comment']


