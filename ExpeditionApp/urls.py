from django.urls import path
from .views import *

app_name = 'expeditions'
urlpatterns =[
    path('create/',ExpeditionCreateView.as_view(), name='create'),
    path('<int:pk>/update/',ExpeditionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',DeleteExpeditionView.as_view(), name='delete'),
    path("",ExpeditionListView.as_view(),name="liste"),
    path('<str:reference>/', ExpeditionDetailView.as_view(), name='detail'),
]



