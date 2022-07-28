from django.urls import path
from . import views

urlpatterns = [
    path('', views.watch_appointment, name='watch_appointment'),
    path('check_reservetion', views.check_reservation, name='check_reservation'),
    path('I_Sinsyak', views.I_Sinsyak, name='Ivan_Sinsyak'),
    path('A_Ivanov', views.A_Ivanov, name='A_Ivanov'),
    path('P_Woodman', views.P_Woodman, name='P_woodman'),
    path('O_Nino', views.O_Nino, name='O_Nino'),
]