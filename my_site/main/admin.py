from django.contrib import admin

# Register your models here.

# admin.py
from django.contrib import admin
from .models import Episode, Video

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('preview','episode_number', 'season_number', 'link', 'description')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('episode_number', 'season_number', 'link')