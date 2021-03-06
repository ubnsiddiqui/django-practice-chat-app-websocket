import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Message, Room, LoggedUser


# Create your views here.
@login_required
def index(request):
    # uid4 = str(uuid.uuid4())
    user = User.objects.all()
    logusr = LoggedUser.objects.all()
    chatrooms = Message.objects.all().values_list('group_name', flat=True).distinct()
    return render(request, 'chat/index.html', {'chatrooms': chatrooms, 'logusrs': logusr, 'users': user})


@login_required
def new_room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    room = Room.objects.filter(name=room_name)
    user = User.objects.all()
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name,
        'room': room,
        'users': user
    })


@login_required
def chat_room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    room = Room.objects.filter(name=room_name)
    user = User.objects.all()
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name,
        'room': room,
        'users' : user
    })