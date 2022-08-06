from django.urls import path
from . import views

urlpatterns = [
    path('check_reservation/', views.check_reservation, name="check_reservation"),
    path('specialist/<int:id>/', views.detail_view_specialist, name="detail_view_specialist"),

]