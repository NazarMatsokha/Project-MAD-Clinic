from .models import Appointment
from django.forms import ModelForm, TextInput, SelectMultiple, DateInput, TimeInput, TextInput, Select, SelectDateWidget

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'cabinet', 'date', 'timeslot', 'patient_name', 'patient_last_name']

        widgets = {
            'doctor': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Вибір лікаря',
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
                'placeholder': 'Ім`я'
            }),

            'patient_last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прізвище'
            })
        }