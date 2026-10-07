from django.db import models
from ExpeditionApp.models import Expedition
from vehiculeApp.models import Vehicule
from EntrepriseApp.models import Entreprise

# Create your models here.
class Offre(models.Model):
    prix=models.DecimalField(max_digits=10,
                             decimal_places=2)
    delai_jours=models.PositiveIntegerField()
    statut=models.CharField(max_length=10,
                            choices=[
                                ('porposee','Porposee'),
                                ('acceptee','Acceptee'),
                                ('refusee','Refusee'),
                                ('annulee','Annulee')
                            ])
    date_proposition=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    expedition=models.ForeignKey('ExpeditionApp.Expedition',
                                 on_delete=models.CASCADE,
                                 related_name='Offre')
    vehicule=models.ForeignKey('VehiculeApp.Vehicule',
                               on_delete=models.CASCADE,
                               related_name='Offre')
    entreprise=models.ForeignKey('EntrepriseApp.Entreprise',
                                 on_delete=models.CASCADE,
                                 related_name='Offre')