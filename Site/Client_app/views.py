from django.shortcuts import render

def main_page(request):
    return render(request, 'Client_app/index.html')

def book_appointment(request):
    return render(request, 'Client_app/booking.html')