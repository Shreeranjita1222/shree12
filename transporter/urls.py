from http.client import ImproperConnectionState
from django.urls import path
# from Bus.transporter.views import BusListView
from transporter.views import   TripListView, TripDetailView
from django.views.generic import ListView
from django.shortcuts import render

urlpatterns= [
    # path('', views.index, name="index"),
    path('', TripListView.as_view(), name="Trip-list"),
    path('detail/<int:pk>/', TripDetailView.as_view(), name="trip_detail" ),
    
    

]