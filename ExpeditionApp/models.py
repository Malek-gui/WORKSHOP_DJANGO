from django.db import models
from EntrepriseApp.models import Entreprise
from django.utils import timezone
from django.core.exceptions import ValidationError


class Expedition(models.Model):
    reference = models.CharField(max_length=20, editable=False)
    date_souhaitee = models.DateField()
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.DecimalField(decimal_places=3, max_digits=10)

    statut = models.CharField(
        max_length=100,
        choices=[
            ('publiee', 'Publiée'),
            ('en_cours', 'En cours'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée'),
            ('attribuee', 'Attribuée')
        ],
        default='publiee'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='expeditions'
    )

    def clean(self):
        super().clean()

        if self.poids_kg is not None and self.poids_kg <= 0:
            raise ValidationError({
                'poids_kg': "Le poids doit être strictement supérieur à 0 kg."
            })

        if self.date_souhaitee and self.date_souhaitee < timezone.now().date():
            raise ValidationError({
                'date_souhaitee': "La date souhaitée ne peut pas être dans le passé."
            })

        if (
            self.entreprise_id
            and self.entreprise.type_entreprise != 'chargeur'
        ):
            raise ValidationError({
                'entreprise': (
                    "Une expédition ne peut être créée que "
                    "par une entreprise de type chargeur."
                )
            })


    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_ref()

        self.full_clean()
        return super().save(*args, **kwargs)


    @classmethod
    def _generate_ref(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"EXP-{annee}-"

        last_elem = (
            cls.objects
            .filter(reference__startswith=prefixe)
            .order_by('-reference')
            .first()
        )

        compteur = (
            int(last_elem.reference.split('-')[-1]) + 1
            if last_elem and last_elem.reference.split('-')[-1].isdigit()
            else 1
        )

        if compteur > 99999:
            raise ValueError(
                f"Limite de 99999 expéditions atteinte pour l'année {annee}."
            )

        return f"{prefixe}{compteur:05d}"

    def __str__(self):
        return self.reference
