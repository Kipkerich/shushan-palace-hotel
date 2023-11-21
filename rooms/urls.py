from django.urls import path, include
from . import views as my_views

urlpatterns = [
   path('', my_views.rooms, name='rooms-url',),
    path('add-room/', my_views.add_room, name='add-room-url'),
]