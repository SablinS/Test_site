from . import views
from django.urls import path

urlpatterns = [
path('', views.home),
path('info/', views.info),
path('cont/', views.cont),
path('episode/', views.episode),
path('season/<int:s>/', views.season),
path('episode/<int:e>/<int:s>/', views.player),
path('rand_ep/', views.rand_ep),
# path('season/<int:s>/<int:e>/', views.player_for_season),
path('episode_player/', views.player),
]