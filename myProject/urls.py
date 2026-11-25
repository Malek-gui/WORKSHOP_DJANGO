
from django.contrib import admin
from django.urls import path, include
from .views import homePage, homePageName
from EntrepriseApp.views import RegistrationView


urlpatterns = [
    path('users/', include("django.contrib.auth.urls")),
    path('users/registration/', RegistrationView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('home/<str:name>/', homePageName, name='home_name'),
    path('expeditions/', include('ExpeditionApp.urls')),
    path("vehicules/", include("VehiculeApp.urls")),
    path("entreprises/",include("EntrepriseApp.urls")),
    path("offres/",include("offreApp.urls"))
]
