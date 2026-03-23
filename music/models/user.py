from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    daily_generation_count = models.PositiveIntegerField(default=0)

    def can_generate_song(self):
        return self.daily_generation_count < 20

    def __str__(self):
        return self.username