from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from .filters import Specialization_filter, Last_name_filter
from .forms import AppointmentForm
from django.contrib import messages
from django.core.paginator import Paginator

def watch_appointment(request):
    doctor = Doctor.objects.all()
    filter_specialization = Specialization_filter(request.GET, queryset=Doctor.objects.all())

    return render(request, 'Doctor_app/watch_appointment.html', {'doctor': doctor, 'list': 'Список лікарів', 'filter_specialization': filter_specialization})

def check_reservation(request):
    reservation = Appointment.objects.all()
    filter_doctor_last_name = Last_name_filter(request.GET, queryset=Appointment.objects.all())

    #paginator = Paginator(reservation, 4)
    #page_num = request.GET.get('page', 1)
    #page_objects = paginator.get_page(page_num)

    paginated_filtered_list = Paginator(filter_doctor_last_name.qs, 4)
    page_number = request.GET.get('page')
    page_objects = paginated_filtered_list.get_page(page_number)


    return render(request, 'Doctor_app/check_reservation.html', {'reservation': reservation, 'page_obj': page_objects, 'doc_filter': filter_doctor_last_name})

def I_Sinsyak(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect('main_page')
        else:
            messages.error(request, 'Данні введені невірно')

    doctor = Doctor.objects.filter(last_name='Сінсяк')

    form = AppointmentForm

    return render(request, 'Doctor_app/ivansinsyak.html', {'form': form, 'doctor': doctor})


def A_Ivanov(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect('main_page')
        else:
            messages.error(request, 'Данні введені невірно')

    doctor = Doctor.objects.filter(last_name='Іванов')

    form = AppointmentForm
    return render(request, 'Doctor_app/arcadiyivanov.html', {'form': form, 'doctor': doctor})

def O_Nino(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect('main_page')
        else:
            messages.error(request, 'Данні введені невірно')

    doctor = Doctor.objects.filter(last_name='Нінйо')

    form = AppointmentForm

    return render(request, 'Doctor_app/olesnino.html', {'doctor': doctor, 'form': form})

def P_Woodman(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect('main_page')
        else:
            messages.error(request, 'Данні введені невірно')

    doctor = Doctor.objects.filter(last_name='Вудмен')

    form = AppointmentForm

    return render(request, 'Doctor_app/panaswoodman.html', {'doctor': doctor, 'form': form})
