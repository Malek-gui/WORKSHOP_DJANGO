import csv
from django.contrib import admin
from django.utils.html import format_html
from .models import Offre
from django.http import HttpResponse

@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="offres.csv"'
    writer = csv.writer(response)
    writer.writerow(['reference_expedition', 'transporteur', 'prix', 'statut'])
    for offre in queryset.select_related('expedition', 'transporteur'):
        writer.writerow([offre.expedition.reference, offre.transporteur.raison_sociale,
        offre.prix, offre.statut])
    return response


"""# Couleur du badge par statut (gris par défaut si un nouveau statut est ajouté et oublié ici).
STATUT_COLORS = {
    'proposee': '#fd7e14',
    'acceptee': '#198754',
    'refusee': '#dc3545',
    'retiree': '#6c757d',
}"""

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    actions = [exporter_offres_csv]
    list_display = (
        'id',
        'date_proposition',
        'expedition',
        'transporteur',
        'vehicule',
        'delai_jours',
        'prix',
        'statut_colore',
        'created_at',
    )

    list_filter = ('statut', 'date_proposition', 'transporteur')
    list_editable = ()
    search_fields = (
        'expedition__reference',
        'transporteur__raison_sociale',
        'vehicule__immatriculation',
    )
    list_per_page = 10
    date_hierarchy = 'created_at'

    readonly_fields = (
        'date_proposition',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Informations generales', {
            'fields': ('date_proposition', 'delai_jours')
        }),
        ('Offre info', {
            'fields': (
                'expedition',
                'vehicule',
                'transporteur',
                'prix',
                'statut',
            )
        }),
        ('Date', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'proposee': '#F0AD4E',
            'acceptee': '#5CB85C',
            'refusee': '#D9534F',
            'retiree': '#777777',
        }

        return format_html(
            '<span style="color:white;background-color:{};'
            'padding:3px 8px;border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999999'),
            obj.get_statut_display(),
        )


"""    def get_readonly_fields(self, request, obj=None):
        # Une offre acceptée engage le transporteur : ses conditions ne bougent plus.
        base = list(self.readonly_fields)
        if obj and obj.statut == 'acceptee':
            return base + ['prix', 'delai_jours']
        return base

    @admin.display(description='Statut', ordering='statut')
    def statut_badge(self, obj):
        color = STATUT_COLORS.get(obj.statut, '#6c757d')
        return format_html(
            '<span style="background-color:{}; color:#fff; padding:2px 10px; '
            'border-radius:10px; font-size:12px; font-weight:600;">{}</span>',
            color, obj.get_statut_display(),
        )

    @admin.action(description="Exporter les offres sélectionnées en CSV")
    def exporter_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="offres.csv"'
        # BOM UTF-8 : sans lui, Excel affiche mal les caractères accentués (é, è...).
        response.write('﻿')

        writer = csv.writer(response)
        writer.writerow([
            'Référence expédition', 'Transporteur', 'Véhicule', 'Prix (TND)',
            'Délai (jours)', 'Statut', 'Date de proposition',
        ])
        for offre in queryset.select_related('expedition', 'transporteur', 'vehicule'):
            writer.writerow([
                offre.expedition.reference,
                offre.transporteur.raison_sociale,
                offre.vehicule.immatriculation,
                offre.prix,
                offre.delai_jours,
                offre.get_statut_display(),
                offre.date_proposition,
            ])
        return response"""