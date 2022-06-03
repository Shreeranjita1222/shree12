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