from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('specialist/', views.specialist, name='specialist'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]