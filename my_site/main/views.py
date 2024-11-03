from django.shortcuts import render
from .models import Episode

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

