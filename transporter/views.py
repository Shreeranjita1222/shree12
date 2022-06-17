from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Trip
from django.views import generic 
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView)
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



def index(request):
    bus=Bus.objects.all()
    trips= Trip.objects.all()
    return render(request, "index.html")





class TripListView(ListView):
    template_name= 'trip_list.html'

    queryset= Trip.objects.select_related("bus").all()
    

class TripDetailView(LoginRequiredMixin, DetailView):
    # specify the model to use
    login_url = 'login'
    redirect_field_name = 'login'
    model = Trip
    template_name= 'trip_detail.html'


@login_required(login_url='login')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = Trip.bus.bus_no
                cost = int(seats_r) * Trip.bus.bus_manufacturer
                source_r = Trip.source
                dest_r = Trip.destination
                
                
                username_r = request.Booking.username
                email_r = request.Booking.email
                
                rem_r = Trip.no_of_seats_left - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'booking.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findbus.html', context)

    else:
        return render(request, 'myapp/findbus.html')