from django.contrib import admin
from .models import Vehicule
# Register your models here.


@admin.register(Vehicule)

class VehiculeAdmin(admin.ModelAdmin):
    pass