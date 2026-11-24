from django.shortcuts import render
from django.http import HttpResponse
from EntrepriseApp.models import Entreprise
from ExpeditionApp.models import Expedition
from offreApp.models import Offre
from VehiculeApp.models import Vehicule


def homePage(request):
    try:
        total_entreprises = Entreprise.objects.count()
        total_chargeurs = Entreprise.objects.filter(type_entreprise='chargeur').count()
        total_transporteurs = Entreprise.objects.filter(type_entreprise='transporteur').count()
        total_expeditions = Expedition.objects.count()
        expeditions_publiees = Expedition.objects.filter(statut='publiee').count()
        total_offres = Offre.objects.count()
        total_vehicules = Vehicule.objects.count()
        vehicules_dispo = Vehicule.objects.filter(disponible=True).count()
        
        dernieres_expeditions = (
            Expedition.objects
            .select_related('entreprise')
            .order_by('-created_at')[:6]
        )
    except Exception:
        total_entreprises = 0
        total_chargeurs = 0
        total_transporteurs = 0
        total_expeditions = 0
        expeditions_publiees = 0
        total_offres = 0
        total_vehicules = 0
        vehicules_dispo = 0
        dernieres_expeditions = []

    context = {
        'total_entreprises': total_entreprises,
        'total_chargeurs': total_chargeurs,
        'total_transporteurs': total_transporteurs,
        'total_expeditions': total_expeditions,
        'expeditions_publiees': expeditions_publiees,
        'total_offres': total_offres,
        'total_vehicules': total_vehicules,
        'vehicules_dispo': vehicules_dispo,
        'dernieres_expeditions': dernieres_expeditions,
    }
    return render(request, 'home.html', context)


def homePageName(request, name):
    return HttpResponse(f"Bienvenue sur TransConnect, {name} !")
