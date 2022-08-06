import django_filters
from django.apps import apps

specialist = apps.get_model('Specialist_app', 'Specialist')

class Specialization_filter(django_filters.FilterSet):
    class Meta:
        model = specialist
        fields = ('speciality', 'speciality')
