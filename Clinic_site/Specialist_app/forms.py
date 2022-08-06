from .models import Appointment
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