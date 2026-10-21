from django.contrib import admin
from .models import Entreprise,User
from django.contrib.auth.admin import UserAdmin
from VehiculeApp.models import Vehicule
# Register your models here.


@admin.register(User) # ou bien admin.site.register(User,AdminUtilisateur) apres class AdminUtilisateur
class AdminUtilisateur(admin.ModelAdmin):
    list_display=('username','user_id','role')
    list_filter=('email',)
    list_editable=('role',)
    search_fields=('email','telephone')
    date_hierarchy='created_at'
    list_per_page=10

#admin.site.register(User,AdminUtilisateur) ICI
#class vehiculeInline(admin.StackedInline):
class vehiculeInline(admin.TabularInline):
    model=Vehicule
    extra=1
    fields=('immatriculation',
        'type_vehicule',
        'capacite_kg',
        'disponible',)

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=('raison_sociale','matricule_fiscal','adresse')
    list_filter=('adresse',)
    #list_editable=('gerant',)
    search_fields=('matricule_fiscal','raison_sociale')
    list_per_page=10
    date_hierarchy='created_at'

    inlines=[vehiculeInline]

    fieldsets=(('Informations generales',{
            'fields':('raison_sociale','matricule_fiscal')
        }),('Entreprise info',{
            'fields':('type_entreprise','adresse','gerant')
        }),('Date',{
            'fields':('created_at','updated_at')
        })
        )
    readonly_fields=('created_at','updated_at')


#admin.site.register(Entreprise)