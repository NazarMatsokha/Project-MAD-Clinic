from .models import Doctor, Appointment
import django_filters


class Specialization_filter(django_filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ('speciality', 'speciality')


class Last_name_filter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ('doctor', 'date')
