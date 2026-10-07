from django.db import models
from EntrepriseApp.models import Entreprise

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=20,
                               unique=True,
                               editable=False)
    ville_depart=models.CharField(max_length=20)
    ville_arrivee=models.CharField(max_length=20)
    poids_kg=models.DecimalField(decimal_places=3,
                                 max_digits=)
    date_souhaitee=models.DateTimeField()
    description=models.TextField()
    statut=models.CharField(max_length=20,
                            choices=[
                                ('publiée','Publiée'),
                                ('attribuée',''),
                                ('encours','Encours'),
                                ('annulée','Annulée'),
                                default='publiee'
                            ])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Entreprise=models.ForeignKey('EntrepriseApp.Entreprise',
                                 on_delete=models.CASCADE,
                                 related_name='Expedition')