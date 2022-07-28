from django.contrib import admin
from .models import Appointment, Doctor, Location

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Location)

