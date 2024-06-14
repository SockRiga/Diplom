from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import CreateView
from .models import Statment, Service, Order
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class= RegistrationForm
    success_url = reverse_lazy('login')

def allService(request):
    services = Service.objects.filter()
    return render(request, 'services.html', {"services": services})

def About(request):
    return render(request, 'about.html')


def allStatment(request):
    statments = Statment.objects.filter()
    return render(request, 'statment/allStatment.html', {"statments": statments})

def CreateStatment(request):
    if request.method == 'POST':
        statment = Order()
        statment.contact = request.POST.get('title')
        statment.description = request.POST.get('description')
        statment.save()
    return render(request, 'statment/createStatment.html')