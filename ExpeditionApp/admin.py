from django.contrib import admin
from .models import Expedition


@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference','date_souhaitee','ville_depart','ville_arrivee','poids_kg','statut','entreprise','created_at',)
    list_filter = ('statut', 'date_souhaitee', 'entreprise')
    list_editable = ('statut',)
    search_fields = ('reference','ville_depart','ville_arrivee','entreprise__raison_sociale',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    readonly_fields = ('reference', 'created_at', 'updated_at')
    
    fieldsets=(('Informations generales',{
            'fields':('reference','date_souhaitee','ville_depart','ville_arrivee')
        }),('Expedition info',{
            'fields':('poids_kg',)
        }),('Date',{
            'fields':('created_at','updated_at')
        })
        )
    readonly_fields=('created_at','updated_at','reference')
