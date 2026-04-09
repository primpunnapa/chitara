from django.db import models
from django.conf import settings
from .library import Library
from .enum import Genre, Mood, Occasion, VoiceTone, GenerationStatus
import uuid

class Song(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='songs')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    audio_url = models.URLField(blank=True)
    task_id = models.CharField(max_length=255, blank=True, null=True)

    genre = models.CharField(max_length=20, choices=Genre.choices)
    mood = models.CharField(max_length=20, choices=Mood.choices)
    occasion = models.CharField(max_length=20, choices=Occasion.choices)
    voice_tone = models.CharField(max_length=20, choices=VoiceTone.choices)

    generation_status = models.CharField(max_length=20, choices=GenerationStatus.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def rename(self, new_title):
        self.title = new_title
        self.save()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)