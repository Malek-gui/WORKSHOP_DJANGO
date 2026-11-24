from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Expedition
from .forms import ExpeditionForm


class ExpeditionListView(ListView):
    model = Expedition
    template_name = "expeditions/liste.html"
    context_object_name = 'expeditions'

    def get_queryset(self):
        statut = self.request.GET.get('statut', 'publiee')
        qs = (
            Expedition.objects
            .select_related('entreprise')
            .order_by('-created_at')
        )
        if statut and statut != 'all':
            qs = qs.filter(statut=statut)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statut_actif = self.request.GET.get('statut', 'publiee')
        context['statut_actif'] = statut_actif
        context['stats'] = {
            'toutes': Expedition.objects.count(),
            'publiee': Expedition.objects.filter(statut='publiee').count(),
            'en_cours': Expedition.objects.filter(statut='en_cours').count(),
            'livree': Expedition.objects.filter(statut='livree').count(),
        }
        return context


class ExpeditionCreateView(CreateView):
    model = Expedition
    template_name = 'expeditions/form.html'
    form_class = ExpeditionForm
    success_url = reverse_lazy('expeditions:liste')


class ExpeditionUpdateView(UpdateView):
    model = Expedition
    template_name = 'expeditions/form.html'
    form_class = ExpeditionForm
    success_url = reverse_lazy('expeditions:liste')


class DeleteExpeditionView(DeleteView):
    model = Expedition
    template_name = "expeditions/confirm_delete.html"
    context_object_name = 'expedition'
    success_url = reverse_lazy('expeditions:liste')


class ExpeditionDetailView(DetailView):
    model = Expedition
    template_name = 'expeditions/detail.html'
    context_object_name = 'expedition'
    slug_field = 'reference'
    slug_url_kwarg = 'reference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Utilisation de related_name='offres' au lieu de l'attribut par défaut offre_set
        context['offres'] = (
            self.object.offres
            .select_related('transporteur', 'vehicule')
            .order_by('-date_proposition')
        )
        return context
