"""from django.urls import path
from .views import *


app_name="offres"
urlpatterns = [
    path('create/',OffreCreateView.as_view(), name='create'),
    path('<int:pk>/update/',OffreUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',DeleteOffreView.as_view(), name='delete'),
    path('',ListOffreView.as_view(), name='liste')
]"""