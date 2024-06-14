from django.contrib import admin
from .models import Statment, Service, Order


admin.site.register(Statment)
admin.site.register(Service)
admin.site.register(Order)