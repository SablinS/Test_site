from . import views
from django.urls import path

urlpatterns = [
path('', views.home),
path('info/', views.info),
path('cont/', views.cont),
path('episode/', views.episode),
path('season1/', views.season1),
path('season2/', views.season2),
path('season3/', views.season3),
]