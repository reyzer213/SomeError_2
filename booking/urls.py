from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),  
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),  
]