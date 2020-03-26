from django.contrib import admin
from .models import Message,Comment
# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text','user_to','user_from','date')