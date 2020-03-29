from django.shortcuts import render
from django import views
from .models import Message
from django.views.generic import ListView


class MessageListView(ListView):
    queryset = Message.objects.all()
    paginate_by = 2
    context_object_name = "messages"

    template_name = 'index.html'




# Create your views here.
