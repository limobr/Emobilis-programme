from django.urls import path
from . import views

app_name = 'templating'

urlpatterns = [
        path('home/', views.home, name="home"), #home url
        path('story/', views.story, name="ourstory"),
        path('team/', views.team, name="ourteam"),
        path('contact/', views.contact, name="contactus"),
]