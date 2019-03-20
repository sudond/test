from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'

class BookmarkDV(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'
# Create your views here.
