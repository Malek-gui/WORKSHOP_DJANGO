from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator, 
from django.core.exceptions import ValidationError


def validate_email(email):
    if not email:
        raise ValidationError("veuillez saisir une adresse email")
    if not email.endswith('@gmail.com'):
        raise ValidationError("format de l'email invalide (@gmail.com)")
    matricule_validator=RegexValidator(
        regex="^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$", message="ivalide"
    )


# Create your models here.
class User(AbstractUser): 
    user_id=models.CharField(max_length=8, 
                              primary_key=True,
                              editable=False)
    email=models.EmailField(unique=True, validators=[validate_email()])
    telephone=models.CharField(max_length=15,
                               blank=True,
                               null=True)
    role=models.CharField(max_length=10,choices=
                          [('chargeur','Chargeur'),
                          ('transporteur','Transporteur'),
                          ('admin','Administrateur')])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Entreprise(models.Model):
    raison_sociale=models.CharField(max_length=100)
    matricule_fiscal=models.CharField(max_length=17,unique=True, validators=[MinValueValidator()])
    type_entreprise=models.CharField(max_length=15,choices=
                                     [('chargeur','Chargeur'),
                                     ('transporteur','Transporteur')],
                                     default='chargeur')
    adresse=models.TextField(validators=[MinValueValidator(20,"une adresse")])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    gerant=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Entreprise")