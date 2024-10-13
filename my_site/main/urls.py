from . import views
from django.urls import path

urlpatterns = [
path('', views.home),
path('info/', views.info),
path('cont/', views.cont),
path('seasons/', views.seasons),
path('seasons/1/', views.s1),
path('seasons/2/', views.s2),
path('seasons/3/', views.s3),
]