from django.db import models

class Genre(models.TextChoices):
    POP = 'POP', 'Pop'
    ROCK = 'ROCK', 'Rock'
    JAZZ = 'JAZZ', 'Jazz'
    RNB = 'RNB', 'R&B'
    CLASSICAL = 'CLASSICAL', 'Classical'
    COUNTRY = 'COUNTRY', 'Country'
    HIPHOP = 'HIPHOP', 'Hip-Hop'
    EDM = 'EDM', 'EDM'


class Mood(models.TextChoices):
    HAPPY = 'HAPPY', 'Happy'
    SAD = 'SAD', 'Sad'
    ENERGETIC = 'ENERGETIC', 'Energetic'
    CALM = 'CALM', 'Calm'
    ROMANTIC = 'ROMANTIC', 'Romantic'


class Occasion(models.TextChoices):
    BIRTHDAY = 'BIRTHDAY', 'Birthday'
    PARTY = 'PARTY', 'Party'
    WEDDING = 'WEDDING', 'Wedding'
    WORKOUT = 'WORKOUT', 'Workout'
    RELAXATION = 'RELAXATION', 'Relaxation'
    MOURNING = 'MOURNING', 'Mourning'
    ANNIVERSARY = 'ANNIVERSARY', 'Anniversary'

class VoiceTone(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    CHILD = 'CHILD', 'Child'

class GenerationStatus(models.TextChoices):
    PENDING = "PENDING"
    TEXT_SUCCESS = "TEXT_SUCCESS"
    FIRST_SUCCESS = "FIRST_SUCCESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"