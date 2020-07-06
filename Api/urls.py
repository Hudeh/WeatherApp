from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="weather"),
    path('all-weather', views.nigeria, name="all-weather"),
]