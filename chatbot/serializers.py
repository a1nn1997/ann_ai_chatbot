from rest_framework import serializers
from chatbot.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'session', 'text', 'created_at', 'user']
