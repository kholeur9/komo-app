from django.urls import path
#from django.contrib.auth.decorators import login_required
from .views import client, connexion, deconnexion


urlpatterns = [
    path('<int:client_id>/', client, name="client"),
    path('connexion/', connexion, name="connexion"),
    path('deconnexion/', deconnexion, name="deconnexion"),
]