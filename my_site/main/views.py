from django.shortcuts import render, get_object_or_404
from .models import Episode, Video, Season
from random import randint, choice

# Create your views here.

def home(request): return render(request, "main/home.html", {"seasons":Season.objects.all()})
def info(request): return render(request, "main/info.html", {"seasons":Season.objects.all()})
def cont(request): return render(request, "main/cont.html", {"seasons":Season.objects.all()})
def episode(request): 
    season = Episode.objects.all()
    seasons = Season.objects.all()
    return render(request, "main/episode.html", {"season":season,"seasons":seasons})
def player(request, e, s): 
    video = get_object_or_404(Video, episode_number=e, season_number=s)
    seasons = Season.objects.all()
    return render(request, "main/episode_player.html", {'video': video,"seasons":seasons})
def season(request, s):
    season = Episode.objects.all().filter(season_number=s)
    seasons = Season.objects.all()
    return render(request, "main/episode.html", {"season":season,"seasons":seasons})
def rand_ep(request):
    s = choice(Season.objects.all())
    s = s.season_number
    l = Episode.objects.all().filter(season_number=s)
    if len(l)==0:
        return rand_ep(request)
    e = choice(Episode.objects.all().filter(season_number=s))
    e = e.episode_number
    print(s,e)
    return player(request, e, s)
