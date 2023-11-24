from django.shortcuts import render


def home(request):
    return  render(request,'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')


# def room(request):
    # return render(request, 'rooms/room.html')


def addRoom (request):
    return render(request, 'rooms/add-room.html')


