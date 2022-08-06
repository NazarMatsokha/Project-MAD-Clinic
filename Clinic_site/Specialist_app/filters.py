from .models import Appointment
import django_filters

class Last_name_filter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ('specialist', 'date')
