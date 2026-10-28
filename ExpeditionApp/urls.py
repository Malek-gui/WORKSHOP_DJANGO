
from django.urls import path
from .views import ExpeditionListView, ExpeditionDetailView

app_name = 'expeditions'

urlpatterns = [
    path('', ExpeditionListView.as_view(), name='liste'),
    path('<str:reference>/', ExpeditionDetailView.as_view(), name='detail'),
]
