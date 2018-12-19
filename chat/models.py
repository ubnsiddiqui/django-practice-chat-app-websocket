from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.TextField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Model to represent user submitted changed to a resource guide
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group_name = models.ForeignKey(Room, related_name='Room',on_delete=models.CASCADE)
    group_name = models.TextField(max_length=150)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String to represent the message
        """

        return self.message


class LoggedUser(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

