from django.contrib import admin
from .models import Offre
# Register your models here.


@admin.register(Offre)

class OffreAdmin(admin.ModelAdmin):
    pass