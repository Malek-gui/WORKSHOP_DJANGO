from django.db import models

# Create your models here.
class Vehicule(models.Model):
    entreprise=models.ForeignKey('EntrepriseApp.Entreprise',
                                 on_delete=models.CASCADE,
                                 related_name='vehicules')
    immatriculation=models.CharField(max_length=10,
                                     unique=True)
    type_vehicule=models.CharField(max_length=20,
                                   choices=[
                                       ('camion porteur','Camion porteur'),
                                       ('fourgon','Fourgon'),
                                       ('camionnette','Camionnette',
                                        'semi-remorque','Semi-remorque')
                                   ])
    capacite_kg=models.PositiveIntegerField()
    disponible=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
