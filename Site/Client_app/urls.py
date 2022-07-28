from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('book_appointment', views.book_appointment, name='book_appointment'),
]