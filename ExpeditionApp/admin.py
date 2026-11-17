from django.contrib import admin,messages
from django.utils import timezone
from django.utils.html import format_html
from .models import Expedition
from offreApp.models import Offre

"""STATUT_COLORS = {
    'publiee': '#0d6efd',
    'en_cours': '#fd7e14',
    'attribuee': '#6f42c1',
    'livree': '#198754',
    'annulee': '#dc3545',
}
"""
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
    extra = 0
    can_delete = False
    show_change_link = True
    def has_add_permission(self, request, obj=None):
        return False



"""class OffreInlineStacked(admin.StackedInline):
    # exactement le même comportement qu'OffreInline (lecture seule, pas d'ajout), seule la mise en forme change (StackedInline = un bloc vertical par offre, au lieu d'une ligne de tableau). 
    model = Offre
    fields = ('transporteur', 'vehicule', 'prix', 'delai_jours', 'statut', 'date_proposition')
    readonly_fields = fields
    extra = 0
    can_delete = False
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False"""

########################################################
"""# Register your models here.
class EnretardFilter(admin.SimpleListFilter):
    title= 'en retard'
    parameter_name= 'en_retard'
    def lookups(self,req,model):
        return [('oui','OUI'),('non','NON')]
    def queryset(self, request, queryset):
        today= timezone.now().date()
        if self.value()=='oui':
            return queryset.filter(statut='publiee', date_souhaitee__lt=today)
        if self.value()=='non':
            return queryset.exclude(statut='publiee', date_souhaitee__lt=today)
        return queryset"""
    
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
"""    @admin.display(description='Statut', ordering='statut')
    def statut_badge(self, obj):
        color = STATUT_COLORS.get(obj.statut, '#6c757d')
        return format_html(
            '<span style="background-color:{}; color:#fff; padding:2px 10px; '
            'border-radius:10px; font-size:12px; font-weight:600;">{}</span>',
            color, obj.get_statut_display(),
        )"""


    
"""    @admin.action(description=" Clôturer les expéditions sélectionnées")
    def make_it_livree(self,req,queryset):
        liste= queryset.filter(statut='en_cours')
        liste_ignored_el=queryset.exclude(statut='en_cours').count()
        errors=[]
        nbr_sucess=0
        for exp in liste:
            exp.statut='livree'
            try:
                exp.save()
                nbr_sucess+=1
            except:
                errors.append(f"{exp.reference} : this expedition had an error")
        if nbr_sucess:
            self.message_user(
                req,
                f"{nbr_sucess} expeditions cloturées",
                messages.SUCCESS
            )
        if liste_ignored_el:
             self.message_user(
                            req,
                            f"{liste_ignored_el} expeditions ignorées",
                            messages.WARNING
                        )
        for e in errors:
            self.message_user( req, e,messages.ERROR)"""

    
