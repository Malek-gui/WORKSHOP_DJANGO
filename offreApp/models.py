from django.db import models
from ExpeditionApp.models import Expedition
from vehiculeApp.models import Vehicule
from EntrepriseApp.models import Entreprise

from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

# Create your models here.
class Offre(models.Model):
    prix=models.DecimalField(max_digits=10,
                             decimal_places=2,
                             validators=[MinValueValidator(Decimal("0.01"))])
    delai_jours=models.PositiveIntegerField(validators=MinValueValidator(1,"minimum 1"))
    statut=models.CharField(max_length=10,
                            choices=[
                                ('porposee','Porposee'),
                                ('acceptee','Acceptee'),
                                ('refusee','Refusee'),
                                ('annulee','Annulee')
                            ], default='porposee')
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

#
    
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError({'entreprise': "une entreprise de type transporteur peut proposer une offre."
            })
        
        if self.vehicule_id and self.entreprise_id:
            if self.vehicule.entreprise_id != self.entreprise_id:
                raise ValidationError({'vehicule': "Le véhicule doit appartenir au transporteur qui propose l'offre."
                })


        if self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError({'expedition': "l'expédition n'accepte plus de nouvelles offres."
            })


        if self.vehicule_id and hasattr(self.vehicule, 'disponible'):
            if not self.vehicule.disponible:
                raise ValidationError({'vehicule': "indisponible."
                })

    def __str__(self):
        return f"Offre {self.pk} - {self.prix} DT"
