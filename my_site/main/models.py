from django.db import models

# Create your models here.

class Episode(models.Model):
    preview = models.ImageField(null = True, blank = True, upload_to = 'preview/')
    episode_number = models.CharField(max_length=20, default = '1')
    season_number = models.DecimalField(max_digits=5, decimal_places=1, default = '1')
    link = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.episode_number

class Video(models.Model):
    episode_number = models.CharField(max_length=20, default = '1')
    season_number = models.DecimalField(max_digits=5, decimal_places=1, default = '1')
    link = models.CharField(max_length=200)
