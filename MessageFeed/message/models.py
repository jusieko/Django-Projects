from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.CharField(max_length=250,)
    user_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciver', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.ForeignKey(Message,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)




