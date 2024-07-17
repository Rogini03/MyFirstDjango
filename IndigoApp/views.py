from django.shortcuts import render,redirect
from .models import Admission
from .forms import AdmissionForm


# Create your views here.
def entry(request):
    adm=Admission.objects.all()
    return render(request, template_name="indigoapp/entryform.html",context={"adm":adm})

def admdetails(request):
    if request.method == "POST":
        cform=AdmissionForm(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect('/indigo/iform/')
    form=AdmissionForm()
    return render(request,template_name="indigoapp/admdetails.html",context={"form":form})

def deletedetails(request,id):
    admd=Admission.objects.get(id=id)
    admd.delete()
    return redirect('/indigo/iform/')

def updatedetails(request,id):
    update=Admission.objects.get(id=id)
    if request.method == "POST":
        updateform = AdmissionForm(request.POST, instance=update)

        updateform.save()
        return redirect('/indigo/iform/')
    return render(request, template_name="indigoapp/updateform.html", context={"update":update})
