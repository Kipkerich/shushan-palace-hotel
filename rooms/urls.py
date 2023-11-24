from django.urls import path
from . import views as my_views

urlpatterns = [
    path('all-room/', my_views.rooms, name='all-room-url',),
    path('add-room/', my_views.add_room, name='add-room-url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_room, name='update-url'),
    path('pay/<id>', my_views.pay, name='pay-url')
]