from django.db import models
from django.contrib.auth.models import User

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add additional fields here
    # Example fields: bio, phone_number, birth_date, etc.
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
