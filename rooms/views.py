from django.shortcuts import render

# Create your views here.
def rooms(request):
    return render(request, 'rooms/room.html')


def add_room(request):
    return render(request,'rooms/add-room.html')


def update_room(request):
    return render(request, 'rooms/update-room.html')