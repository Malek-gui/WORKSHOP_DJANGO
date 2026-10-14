from django.contrib import admin
from .models import Expedition

# Register your models here.

@admin.register(Expedition)

class ExpeditionAdmin(admin.ModelAdmin):
    pass