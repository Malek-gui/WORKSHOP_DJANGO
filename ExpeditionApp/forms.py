from django import forms
from .models import Expedition
from EntrepriseApp.models import Entreprise

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields = [
            'entreprise',
            'ville_depart',
            'ville_arrivee',
            'date_souhaitee',
            'poids_kg',
            'statut'
        ]
        labels = {
            'entreprise': 'Entreprise (Chargeur)',
            'ville_depart': 'Ville de départ',
            'ville_arrivee': "Ville d'arrivée",
            'date_souhaitee': 'Date souhaitée de livraison',
            'poids_kg': 'Poids de la marchandise (kg)',
            'statut': 'Statut de l\'expédition',
        }
        widgets = {
            'date_souhaitee': forms.DateInput(attrs={'type': 'date'}),
            'poids_kg': forms.NumberInput(attrs={'step': '0.001', 'min': '0.001', 'placeholder': 'Ex: 1250.500'}),
            'ville_depart': forms.TextInput(attrs={'placeholder': 'Ex: Tunis, Sfax...'}),
            'ville_arrivee': forms.TextInput(attrs={'placeholder': 'Ex: Sousse, Bizerte...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seules les entreprises de type chargeur peuvent créer des expéditions
        self.fields['entreprise'].queryset = Entreprise.objects.filter(type_entreprise='chargeur')
