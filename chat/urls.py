from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<str:room_name>/', views.new_room, name='new_room'),
    path('chat_room/<str:room_name>', views.chat_room, name='chat_room'),
]
