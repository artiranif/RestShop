from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Commande
from .models import Enseigne
from .models import Marque
from .models import Produits


def limiteurmarque(serialiseur: serializers.HyperlinkedModelSerializer, marque: str):
    """ Limite le choix de l'utilisateur à ses marques
    :param serialiseur: generalement self
    :param marque: précise le nom de la marque selon la table
    """
    request_user = serialiseur.context['request'].user
    if Marque.estproprietaire(request_user):
        serialiseur.fields[marque].queryset = Marque.objects.filter(proprietaires=request_user)


class CommandesSerialiseur(serializers.HyperlinkedModelSerializer):
    proprietaire = serializers.ReadOnlyField(source='proprietaire.username')
    produits = serializers.SlugRelatedField(queryset=Produits.objects.all(), many=True, slug_field='nomProduits')

    class Meta:
        model = Commande
        fields = ['url','proprietaire','produits']


class EnseigneSerialiseur(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        limiteurmarque(self, 'marqueEnseigne')

    class Meta:
        model = Enseigne
        fields = ['url', 'adresse', 'nomEnseigne', 'marqueEnseigne', 'produitPhare']


class MarqueSerialiseur(serializers.HyperlinkedModelSerializer):
    proprietaires = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Marque
        fields = ['url', 'nomMarque', 'proprietaires']


class ProduitSerialiseur(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        limiteurmarque(self,'marqueProduits')

    class Meta:
        model = Produits
        fields = ['url', 'description', 'nomProduits', 'marqueProduits', 'prix']

