from django.db import models
from EntrepriseApp.models import Entreprise
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=13,
                               unique=True,
                               editable=False)
    ville_depart=models.CharField(max_length=20)
    ville_arrivee=models.CharField(max_length=20)

    poids_kg=models.DecimalField(decimal_places=3,
                                 max_digits=10,
                                 validators=[MinValueValidator(Decimal("0.001"))])
    
    date_souhaitee=models.DateTimeField()
    description=models.TextField()
    statut=models.CharField(max_length=20,
                            choices=[
                                ('publiée','Publiée'),
                                ('attribuée',''),
                                ('encours','Encours'),
                                ('annulée','Annulée'),
                            ],default="publiee"
                            )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Entreprise=models.ForeignKey('EntrepriseApp.Entreprise',
                                 on_delete=models.CASCADE,
                                 related_name='Expedition')

    def save(self,*args,**kwargs):
        self.reference=self.generate_ref()
        return super().save(*args,**kwargs)
    @classmethod
    def _generate_ref(cls):
        annee = timezone.now().strftime('%Y') #RQ: Y #4 chiffres et y #2 chiffres
        prefix=f"EXP-{annee}-"
        last_element=(cls.objects.filter(reference_startswith=prefix).order_by('-reference').first()) #si descendant LAST
        compteur= int(last_element.reference[-5:])+1 if last_element else 1

        if compteur > 99999:
            raise ValueError(f"limite de 99999 pour annee {annee}")
        return f"{prefix}{compteur:05d}"

#
    def __str__(self):
        return self.reference

    def clean(self):
        super().clean()
        if self.entreprise_id:
            if self.entreprise.type_entreprise != "chargeur":
                raise ValidationError({
                    "entreprise": (
                        "Une expédition doit appartenir à un chargeur."
                    )
                })