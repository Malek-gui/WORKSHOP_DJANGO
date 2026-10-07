# AI_LOG

## Entrée [06/10/2026] - Outil IA utilisé : ChatGPT

* **Prompt :**
  Identifier les 4 anomalies présentes dans le premier jet du modèle Django `Offre`, les corriger et justifier les corrections par rapport au cahier des charges.

* **Sortie obtenue (résumé) :**
  L'assistant IA a analysé le modèle `Offre` et a proposé des corrections concernant le type du prix, la date de proposition, la suppression du véhicule associé et la méthode `save()`.

+
* **Écarts identifiés vs cahier des charges :**

  1. Le champ `prix` était défini avec un `CharField`, alors qu'il doit représenter une valeur numérique.
  2. Le champ `date_proposition` utilisait `auto_now=True`, ce qui modifie la date lors de chaque modification de l'offre.
  3. Le champ `vehicule` utilisait `on_delete=models.CASCADE`, ce qui peut supprimer l'offre lorsque le véhicule est supprimé.
  4. La méthode `save()` redéfinie ne contenait aucune logique supplémentaire.

* **Correction apportée et justification :**

  1. Remplacement de `CharField` par `DecimalField(max_digits=10, decimal_places=2)` afin de stocker correctement le prix.
  2. Remplacement de `auto_now=True` par `auto_now_add=True` afin de conserver la date de création de l'offre.
  3. Remplacement de `on_delete=models.CASCADE` par `on_delete=models.SET_NULL` avec `null=True` afin de conserver l'offre si le véhicule est supprimé.
  4. Suppression de la méthode `save()` car elle est inutile dans ce cas.

* **Commit associé :**
  `AI: ajout initial du modèle Offre assisté par IA`

* **Commit de correction :**
  `Review: correction des anomalies du modèle Offre`
