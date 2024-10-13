from django.shortcuts import render
from .models import Episode

# Create your views here.

def home(request): return render(request, "main/home.html")
def info(request): return render(request, "main/info.html")
def cont(request): return render(request, "main/cont.html")
def seasons(request): return render(request, "main/seasons.html")
def s1(request): 
    season = Episode.objects.all()
    return render(request, "main/season1.html", {"season":season})
def s2(request): return render(request, "main/season2.html")
def s3(request): return render(request, "main/season3.html")


