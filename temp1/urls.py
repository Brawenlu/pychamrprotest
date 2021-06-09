from django.urls import path
from .views import *
urlpatterns = [
    path('zhuce',zhuce),
    path('add',addusers),
    path('md5.js',md5js),
    path('h5.html',h5)
]