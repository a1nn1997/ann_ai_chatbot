from django.contrib import admin
from chatbot.models import ChatSession, Message
# Register your models here.

admin.site.register(ChatSession)
admin.site.register(Message)