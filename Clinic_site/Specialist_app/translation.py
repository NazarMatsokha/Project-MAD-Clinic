from modeltranslation.translator import register, TranslationOptions
from .models import Appointment, Specialist, Location

@register(Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name', 'speciality', 'description')

@register(Location)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ('cabinet',)
