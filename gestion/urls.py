from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
routeur = DefaultRouter()
routeur.register(r'commandes', views.CommandeVue)
routeur.register(r'enseignes', views.EnseigneVue)
routeur.register(r'marques', views.MarqueVue)
routeur.register(r'produits', views.ProduitVue)

urlpatterns = [
    path('', include(routeur.urls)),
]
