from django.shortcuts import render
from django.views.generic   import CreateView,ListView,UpdateView,DeleteView
from .models import Offre
from django.urls import reverse_lazy
from .forms import OffreForm


"""
# Create your views here.
class OffreCreateView(CreateView):
    model= Offre
    template_name ='offres/form.html'
    #fields ='__all__'
    form_class = OffreForm
    success_url = reverse_lazy('offres:liste')
class OffreUpdateView(UpdateView):
    model= Offre
    template_name ='offres/form.html'
    #fields ='__all__'
    form_class = OffreForm
    success_url = reverse_lazy('offres:liste')
class ListOffreView(ListView):
    model= Offre
    template_name="offres/liste.html"
    context_object_name ='offres'
class DeleteOffreView(DeleteView):
    model=Offre
    template_name ="offres/confirm_delete.html"
    context_object_name ='offre'
    success_url = reverse_lazy('offres:liste')
"""