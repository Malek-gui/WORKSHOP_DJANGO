
from django.views.generic import ListView, DetailView
from .models import Expedition


class ExpeditionListView(ListView):
    model = Expedition
    template_name = 'expeditions/liste.html'
    context_object_name = 'expeditions'

    def get_queryset(self):
        return (
            Expedition.objects
            .filter(statut='publiee')
            .select_related('entreprise')
            .order_by('-created_at')
        )


class ExpeditionDetailView(DetailView):
    model = Expedition
    template_name = 'expeditions/detail.html'
    context_object_name = 'expedition'
    slug_field = 'reference'
    slug_url_kwarg = 'reference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offres'] = (
            self.object.offre_set
            .select_related('transporteur', 'vehicule')
        )
        return context
