from django.shortcuts import render, redirect
from .models import Appointment, Specialist
from .filters import Last_name_filter
from django.core.paginator import Paginator
from .forms import AppointmentForm
from django.contrib import messages


def check_reservation(request):
    reservation = Appointment.objects.all()
    filter_specialist_last_name = Last_name_filter(request.GET, queryset=Appointment.objects.all())

    paginated_filtered_list = Paginator(filter_specialist_last_name.qs, 4)
    page_number = request.GET.get('page')
    page_objects = paginated_filtered_list.get_page(page_number)

    return render(request, 'Specialist_app/check_reservation.html', {'reservation': reservation, 'page_obj': page_objects, 'doc_filter': filter_specialist_last_name})

def detail_view_specialist(request, id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect('main_page')
        else:
            messages.error(request, 'Данні введені невірно')

    objct = Specialist.objects.get(id=id)



    form = AppointmentForm

    return render(request, 'Specialist_app/detail_view_specialist.html', {'form': form, 'objct':objct})


