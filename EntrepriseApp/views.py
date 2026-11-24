from django.shortcuts import render
from django.views.generic   import CreateView,ListView,UpdateView,DeleteView
from .models import Entreprise
from django.urls import reverse_lazy
from .forms import EntrepriseForm



# Create your views here.
class EntrepriseCreateView(CreateView):
    model= Entreprise
    template_name ='entreprises/form.html'
    #fields ='__all__'
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprises:liste')


class EntrepriseUpdateView(UpdateView):
    model= Entreprise
    template_name ='entreprises/form.html'
    #fields ='__all__'
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprises:liste')


class ListEntrepriseView(ListView):
    model= Entreprise
    template_name="entreprises/liste.html"
    context_object_name ='entreprises'


class DeleteEntrepriseView(DeleteView):
    model=Entreprise
    template_name ="entreprises/confirm_delete.html"
    context_object_name ='entreprise'
    success_url = reverse_lazy('entreprises:liste')
