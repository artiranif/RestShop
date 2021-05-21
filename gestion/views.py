from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from .serializers import *
from .permissions import *

# CustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

MV = viewsets.ModelViewSet


class CommandeVue(MV):
    queryset = Commande.objects.all()
    serializer_class = CommandesSerialiseur
    permission_classes = [PermissionCommande]
    
    # ProprioCommande
    def perform_create(self, serializer):
        serializer.save(proprietaire=self.request.user)


class EnseigneVue(MV):
    queryset = Enseigne.objects.all()
    serializer_class = EnseigneSerialiseur
    permission_classes = [PermissionEnseigne]


class MarqueVue(MV):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerialiseur
    permission_classes = [PermissionMarque]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *argsn, **kwrgs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class ProduitVue(MV):
    queryset = Produits.objects.all()
    serializer_class = ProduitSerialiseur
    permission_classes = [PermissionProduit]


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
