from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
        path('', views.index_page, name="home"),
        path('story/', views.story, name="mystory"),
        path('team/', views.team, name="team"),
        path('contact/', views.contact, name="contact"),
]