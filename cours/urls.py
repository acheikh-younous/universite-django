from django.urls import path
from ..views import liste_cours, acceuil, ajouter_cours, modifier_cours, supprimer_cours, connexion_utilisateur, deconnexion_utilisateur
urlpatterns = [
    path('', acceuil, name='accueil'),
    path('cours/', liste_cours, name='liste_cours'),
    path('ajouter/', ajouter_cours, name='ajouter_cours'),
    path('modifier/<int:id>/', modifier_cours, name='modifier_cours'),
    path('supprimer/<int:id>/', supprimer_cours, name='supprimer_cours'),
    path('connexion/', connexion_utilisateur, name='connexion'),
    path('deconnexion/', deconnexion_utilisateur, name='deconnexion'),

]
