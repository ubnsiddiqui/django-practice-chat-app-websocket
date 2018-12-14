import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Message


# Create your views here.
@login_required
def index(request):
    uid4 = str(uuid.uuid4())
    user = User.objects.all()
    return render(request, 'chat/index.html', {'uid4': uid4,'users':user})


@login_required
def room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name
    })
