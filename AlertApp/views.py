from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def alert(request):
    return render(request,template_name="alertapp/alert.html")

def success(request):
    messages.success(request, message="This is a success messages")
    return render(request, template_name="alertapp/alert.html")

def error(request):
    messages.error(request, message="This is a error messages")
    return render(request, template_name="alertapp/alert.html")

def info(request):
    messages.info(request, message="This is a information messages")
    return render(request, template_name="alertapp/alert.html")

def warning(request):
    messages.warning(request, message="This is a warning messages")
    return render(request, template_name="alertapp/alert.html")
