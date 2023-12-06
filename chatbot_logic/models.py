from django.db import models
from django.conf import settings

# Create your models here.
class TrainingData(models.Model):
    input_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TrainingData {self.id}"

class UserPreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preferences = models.JSONField()  # This field can store various user preferences

    def __str__(self):
        return f"Preferences for {self.user.username}"
