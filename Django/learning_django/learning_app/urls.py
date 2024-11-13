from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_home, name='home'),
    path('story/', views.story_view, name='story'),
    path('team/', views.team_view, name='team'),
    path('contact/', views.contact_view, name='contact'),
]