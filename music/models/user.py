from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    daily_generation_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_generate_song(self):
        return self.daily_generation_count < 20

    def __str__(self):
        return self.username