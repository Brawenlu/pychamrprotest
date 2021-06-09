from django.shortcuts import render

# Create your views here.
from .models import *

# Create your views here.
def zhuce(request):
    if request.method=="POST":
        zc = Zhuce()
        zc.user=request.POST.get("user")
        zc.pwd=request.POST.get("pwd")
        zc.sex=request.POST.get('gender')
        zc.married=request.POST.get('wedding')
        zc.hobby=request.POST.getlist('trip')
        zc.introduction=request.POST.get('text1')
        zc.age=request.POST.get('age')
        zc.save()
        return render(request, 'temp1/show.html', {})
    else:
        return render(request, 'temp1/rege.html', {})

def addusers(request):
    return render(request,"temp1/UserOpt.html", {})

def md5js(request):
    return render(request,'temp1/md5.js', {})

def h5(request):
    return  render(request,'temp1/h5.html', {})

