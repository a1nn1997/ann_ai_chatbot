from django.db import models
from django.conf import settings

class ChatSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session {self.id} - User {self.user.username}"


class Message(models.Model):
    USER=1
    BOT=1
    MESSAGE_TYPE=(
        ("USER", USER),
        ("BOT", BOT),
    )
    message_type = models.SmallIntegerField(choices=MESSAGE_TYPE, default=USER)
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message {self.id} in {self.session}"


class MessageResponse(models.Model):
    input_text = models.TextField()
    output_text = models.JSONField()

