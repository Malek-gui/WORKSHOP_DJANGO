
from django.contrib import admin
from django.utils.html import format_html
from .models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):

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
