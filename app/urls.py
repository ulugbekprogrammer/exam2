from django.urls import path
from .views import *

urlpatterns = [
    path('home', home),
    path('bot/', bot_view, name='bot_view'),
]