from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
from page.models import services,massage,footer_Massage
#from .forms import getMassage

# Create your views here.

def Home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mass = request.POST['mass']

        massagees = massage(name = name, email = email ,  mass = mass )
        massagees.save()

    post = services.objects.all()
    contex = { 'post' :post }
    return render(request, 'index.html',contex )
def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mass = request.POST['mass']

        massagees = massage(name = name, email = email ,  mass = mass )
        massagees.save()
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mass = request.POST['mass']

        massagees = massage(name = name, email = email ,  mass = mass )
        massagees.save()
    return render(request, "contact.html")


def service(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mass = request.POST['mass']

        massagees = massage(name = name, email = email ,  mass = mass )
        massagees.save()
    return render(request, "services.html")

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mass = request.POST['mass']

        massagees = massage(name = name, email = email ,  mass = mass )
        massagees.save()

    return render(request, "register.html")



'''
def one(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        tolk = request.POST['tolk']
        foter = footer_Massage(name = name , email = email, tolk = tolk)
        foter.save()
    return render(request, "base.html")

def two(request):
    return render(request, "one.html")'''