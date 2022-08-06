from django.contrib import admin
from .models import Appointment, Specialist, Location
from modeltranslation.admin import TranslationAdmin

admin.site.register(Appointment)
@admin.register(Specialist)
class SpecialistAdmin(TranslationAdmin):
    pass
@admin.register(Location)
class SpecialistAdmin(TranslationAdmin):
    pass
