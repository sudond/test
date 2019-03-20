from django.urls import path
from . import views
from .models import Bookmark
from django.views.generic import ListView, DetailView
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
]