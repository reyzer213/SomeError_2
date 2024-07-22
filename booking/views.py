from django.shortcuts import render, get_object_or_404
from .models import Room, Booking

def index(request):
    rooms = Room.objects.all()
    return render(request, 'booking/index.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'booking/room_detail.html', {'room': room})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})
