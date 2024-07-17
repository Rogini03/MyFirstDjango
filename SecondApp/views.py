import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import StudentDetails
from .forms import RegisterForm



# Create your views here.
def second(request):
    return HttpResponse("<h1>This is second app</h1>")


def ipltable(request):
    time = datetime.datetime.now
    return render(request, template_name="secondapp/ipltable.html", context={"name": "Ramu", "time": time})


def PriceDetails(request):
    return render(request, template_name="secondapp/pricedetails.html")


def totalprice(request):
    mobile = int(request.GET["mobiles"])
    keyboard = int(request.GET["keyboard"])
    mouse = int(request.GET["mouse"])
    pendrive = int(request.GET["pendrive"])
    totalprice = mobile+keyboard+mouse+pendrive
    return render(request, template_name="secondapp\\totalprice.html", context={"totalprice": totalprice})

def stddetail(request):
    students = StudentDetails.objects.all()
    return render(request, template_name="secondapp\\stddetail.html", context={"students":students})

def studentregister(request):
    if(request.method=="POST"):
        if (request.POST.get("stdname")
            and request.POST.get("stdclass")
            and request.POST.get("stdsection")
            and request.POST.get("joindate")):
            register = StudentDetails()
            register.stdname = request.POST.get("stdname")
            register.stdclass = request.POST.get("stdclass")
            register.stdsection = request.POST.get("stdsection")
            register.joindate = request.POST.get("joindate")
            register.save()
            return HttpResponse("<h2>Data saved successfully <a href='/second/getstd/'>Click here</a> to see the list")
    forms = RegisterForm()
    return render(request, template_name="secondapp\\registerform.html", context={"forms": forms})
