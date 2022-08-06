from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.apps import apps
from .filters import Specialization_filter

specialist1 = apps.get_model('Specialist_app', 'Specialist')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно зареєструвались')
            return redirect('login')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    return render(request, 'Client_app/register.html', {"form": form})

def login_user(request):
    form_class = UserLoginForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            form = UserLoginForm()
    return render(request, 'Client_app/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('main_page')

def main_page(request):
    return render(request, 'Client_app/index.html')

def specialist(request):
    specialist = specialist1.objects.all()
    filter_specialization = Specialization_filter(request.GET, queryset=specialist1.objects.all())

    return render(request, 'Client_app/specialist.html', {'specialist': specialist, 'list': 'Список лікарів', 'filter_specialization': filter_specialization})
