from django.contrib import admin
from .models import Entreprise,User
from django.contrib.auth.admin import UserAdmin
# Register your models here.



@admin.register(User) # ou bien admin.site.register(User,AdminUtilisateur) apres class AdminUtilisateur
class AdminUtilisateur(admin.ModelAdmin):

    list_display=('username','user_id','role')
    list_filter=('email',)
    list_editable=('role',)
    search_fields=('email','telephone')
    list_per_page=10
    date_hierarchy='created_at'


#admin.site.register(User,AdminUtilisateur) ICI


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=('raison_sociale','matricule_fiscal','adresse')
    #list_filter=('adresse',)
    #list_editable=('role',)
    #search_fields=('email','telephone')
    list_per_page=10
    date_hierarchy='created_at'


#admin.site.register(Entreprise)