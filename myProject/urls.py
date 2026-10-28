
from django.contrib import admin
from django.urls import path, include
from .views import homePage, homePageName

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('home/<str:name>/', homePageName, name='home_name'),
    path('expeditions/', include('ExpeditionApp.urls')),
]
