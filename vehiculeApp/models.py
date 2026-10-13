from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

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
    capacite_kg=models.PositiveIntegerField(validators=[MinValueValidator(1,"une capacité NULL ne peut pas etre acceptée"),MinValueValidator(1000,"capacité ne dépasse pas 1000")])
    disponible=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError("un vehicule ne peut être rattaché qu'au transporteur")

#
    def __str__(self):
        return f"{self.immatriculation} - {self.get_type_vehicule_display()}"