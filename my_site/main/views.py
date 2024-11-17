from django.shortcuts import render, get_object_or_404
from .models import Episode, Video


# Create your views here.

def home(request): return render(request, "main/home.html")
def info(request): return render(request, "main/info.html")
def cont(request): return render(request, "main/cont.html")
def episode(request): 
    season = Episode.objects.all()
    return render(request, "main/episode.html", {"season":season})
def season1(request): 
    season = Episode.objects.filter(season_number = 1)
    return render(request, "main/episode.html", {"season":season})
def season2(request): 
    season = Episode.objects.filter(season_number = 2)
    return render(request, "main/episode.html", {"season":season})
def season3(request): 
    season = Episode.objects.filter(season_number = 3)
    return render(request, "main/episode.html", {"season":season})
def player(request): return render(request, "main/episode_player.html")
def players1e1(request): 
    video = get_object_or_404(Video, episode_number=1, season_number=1)
    return render(request, 'episode_player.html', {'video': video})
