from django.db import models

# Create your models here.

class Episode(models.Model):
    preview = models.ImageField(null = True, blank = True, upload_to = 'preview/')
    episode_number = models.PositiveIntegerField()
    season_number = models.PositiveIntegerField()
    link = models.CharField(max_length=200)
    description = models.TextField()

class Video(models.Model):
    episode_number = models.PositiveIntegerField()
    season_number = models.PositiveIntegerField()
    link = models.FileField(null = True, blank = True, upload_to = 'video/')

class Season(models.Model):
    season_number = models.PositiveIntegerField()