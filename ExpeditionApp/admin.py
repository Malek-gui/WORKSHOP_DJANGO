
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Expedition
from offreApp.models import Offre

##########################################################
class enRetardFilter(admin.SimpleListFilter):
    title = 'En retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return [
            ('oui', 'OUI'),
            ('non', 'NON'),
        ]

    def queryset(self, request, queryset):
        today = timezone.now().date()

        if self.value() == 'oui':
            return queryset.filter(
                statut='publiee',
                date_souhaitee__lt=today
            )

        if self.value() == 'non':
            return queryset.exclude(
                statut='publiee',
                date_souhaitee__lt=today
            )

        return queryset


class offreInline(admin.TabularInline):
    model=Offre
    extra=0
    fields= (
        'transporteur',
        'vehicule',
        'delai_jours',
        'prix',
        'statut',
        'date_proposition',
    )
    readonly_fields = fields

    
##########################################################
@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):

    list_display = (
        'statut_colore',
        'reference',
        'date_souhaitee',
        'ville_depart',
        'ville_arrivee',
        'poids_kg',
        'statut',
        'entreprise',
        'created_at',
    )

    list_filter = (
        'statut',
        'date_souhaitee',
        'entreprise',
        enRetardFilter,
    )

    list_editable = ('statut',)

    search_fields = (
        'reference',
        'ville_depart',
        'ville_arrivee',
        'entreprise__raison_sociale',
    )

    list_per_page = 10
    date_hierarchy = 'created_at'

    readonly_fields = (
        'reference',
        'created_at',
        'updated_at',
    )
    inlines=[offreInline]
    fieldsets = (
        ('Informations generales', {
            'fields': (
                'entreprise',
                'reference',
                'date_souhaitee',
                'ville_depart',
                'ville_arrivee',
            )
        }),
        ('Expedition info', {
            'fields': ('poids_kg',)
        }),
        ('Date', {
            'fields': ('created_at', 'updated_at')
        }),
    )



    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'publiee': '#0275D8',
            'en_attente': '#F0AD4E',
            'en_cours': '#5CB85C',
            'livree': '#5CB85C',
            'annulee': '#D9534F',
        }

        return format_html(
            '<span style="color:white; background-color:{}; '
            'padding:3px 8px; border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999999'),
            obj.get_statut_display(),
        )
