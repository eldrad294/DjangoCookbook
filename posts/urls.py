from django.urls import path
from .views import HomePageView2

urlpatterns = [
    path('', HomePageView2.as_view(), name='home2'),
    path('home2/', HomePageView2.as_view(), name='home2')
]