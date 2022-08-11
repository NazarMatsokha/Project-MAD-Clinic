from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, Specialist, Comments
from .filters import Last_name_filter
from django.core.paginator import Paginator
from .forms import AppointmentForm, CommentsForm
from django.contrib import messages



def check_reservation(request):
    reservation = Appointment.objects.all()
    filter_specialist_last_name = Last_name_filter(request.GET, queryset=Appointment.objects.all())

    paginated_filtered_list = Paginator(filter_specialist_last_name.qs, 4)
    page_number = request.GET.get('page')
    page_objects = paginated_filtered_list.get_page(page_number)

    return render(request, 'Specialist_app/check_reservation.html', {'reservation': reservation, 'page_obj': page_objects, 'doc_filter': filter_specialist_last_name})



def detail_view_specialist(request, id):
    objct = Specialist.objects.get(id=id)


    # registration form
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно подали заявку')
            return redirect("detail_view_specialist", id=id)
        else:
            messages.error(request, 'Данні введені невірно')

    # commentaries form
    specialist = get_object_or_404(Specialist, id=id)
    comments = Comments.objects.filter(specialist=id)
    comment_form = CommentsForm(data=request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            content = request.POST.get('comment')
            comment = Comments.objects.create(specialist = specialist, author = request.user, comment = content)
            comment.save()
            return redirect('detail_view_specialist', id=id)
        else:
            comment_form = CommentsForm


    form = AppointmentForm

    return render(request, 'Specialist_app/detail_view_specialist.html', {'form': form, 'objct':objct, 'comment_form':comment_form,
                                                                          'comments': comments})


