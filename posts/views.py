from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomePageView2(ListView):
    model = Post
    template_name = 'home2.html'
    context_object_name = 'all_posts_list'