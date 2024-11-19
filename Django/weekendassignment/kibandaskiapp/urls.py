from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book_table/', views.book_table, name='book_table'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('show_bookings', views.retrieve_bookings, name= 'show_bookings'),
    path('delete/<int:id>/', views.delete_booking, name= 'delete_booking'),
    path('edit/<int:booking_id>/', views.update_booking, name="update_booking"),


]