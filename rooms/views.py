from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RoomForm
from django.contrib import messages
from .models import Room
from .credentials import *

# Create your views here.
def rooms(request):
    all_rooms = Room.objects.all()
    context = {'rooms': all_rooms}
    return render(request, 'rooms/room.html', context)


def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful')
            return redirect("add-room-url")
        else:
            messages.error(request, 'Failed')
            return redirect("add-room-url")
    else:
        form = RoomForm()
    return render(request, 'rooms/add-room.html', {'form': form})


def update_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == "POST":
        room_name = request.POST.get('name')
        room_size = request.POST.get('size')
        room_price = request.POST.get('price')
        room_desc = request.POST.get('desc')
        room_image = request.FILES.get('image')
        room.name = room_name
        room.size = room_size
        room.price = room_price
        room.desc = room_desc
        room.image = room_image
        room.save()
        messages.success(request, 'Room details updated successfully')
        return redirect('all-room-url')
    return render(request, 'rooms/update-room.html', {'room': room})


def delete(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    messages.success(request, 'Room removed successfully')
    return redirect('all-room-url')


def pay (request, id):
    room = Room.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST['phone-number']
        amount = room.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "Hotel reservation"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success")
    return render(request, 'rooms/pay.html', {'room': room})
