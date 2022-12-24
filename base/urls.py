from django.urls import path
from .views import (lobby, room, getToken, createMember,
                    getMember, deleteMember)

urlpatterns = [
    path('', lobby, name='lobby'),
    path('room/', room, name='room'),
    path('get_token/', getToken, name='get_token'),
    path('create_member/', createMember, name='create-member'),
    path('get_member/', getMember, name='get-member'),
    path('delete_member/', deleteMember, name='delete-member'),
]
