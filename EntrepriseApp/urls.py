from django.urls import path
from .views import *


app_name="entreprises"
urlpatterns = [
    path('create/',EntrepriseCreateView.as_view(), name='create'),
    path('<int:pk>/update/',EntrepriseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',DeleteEntrepriseView.as_view(), name='delete'),
    path('',ListEntrepriseView.as_view(), name='liste')
]