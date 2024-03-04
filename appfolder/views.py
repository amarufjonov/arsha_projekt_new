from django.shortcuts import render


# Create your views here.
from appfolder.models import *


def index(request):
    servis=Servis.objects.all()
    portfilo=Portfolio.objects.all()
    team=Team.objects.all()
    return render(request, 'index.html',{"servis":servis,"portfilo":portfilo,"team":team})


def portfilo(malumot):
    return render(malumot, 'portfolio-details.html')


def inner_page(malumot):
    return render(malumot, 'inner-page.html')



def contact(malumot):
    if malumot.method=="POST":
        ism = malumot.POST.get('ism')
        email = malumot.POST.get('e-pochta')
        yonalish = malumot.POST.get('fan')
        malumott = malumot.POST.get('xabar')
        Contact(ism=ism,yonalish=yonalish,malumot=malumott,email=email).save()
    contact = Contact.objects.all()
    return render(malumot,'index.html',{"contact":contact})