from django.shortcuts import render
from .models import *
def add(request):
    if request.method=='POST':
        zc=Zhuce()
        zc.name=request.POST.get('username')
        zc.pwd = request.POST.get('pwd')