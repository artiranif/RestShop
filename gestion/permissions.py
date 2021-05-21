from rest_framework import permissions

from .models import Commande, Produits, Enseigne, Marque


class PermissionGeneral(permissions.BasePermission):
    """ Cette permission permet la lecture de tout les éléments"""
    @staticmethod
    def visible(request):
        """
            Tous les modèles sont disponibles à la lecture pour tous les utilisateurs (même non
            authentifiés).
            Appliquer sur tous
        """
        return request.method in permissions.SAFE_METHODS

    def has_permission(self, request, view):
        return PermissionGeneral.visible(request) or self.permissionspecial(request, view)

    def has_object_permission(self, request, view, obj):
        return PermissionGeneral.visible(request) or self.permissionspecialobjet(request, view, obj)

    def permissionspecial(self, request, view):
        """ Equivalent de has_permission."""
        return False

    def permissionspecialobjet(self, request, view, obj):
        """ Equivalent de has_object_permission."""
        return False


def DEL(request):
    """ Permet de supprimer un élément. """
    return request.method == 'DELETE'


def PUT(request):
    """ Permet de modifier un élément. """
    return request.method == 'PUT'


def POST(request):
    """ Permet de créer un élément"""
    return request.method == 'POST'



def staffAll(request):
    """
    Seul le staff peut créer, modifier et supprimer
    appliquer sur : marque et enseigne
    """
    return request.user and request.user.is_staff


class PermissionMarque(PermissionGeneral):
    def permissionspecial(self, request, view):
        return staffAll(request)


class PermissionCommande(PermissionGeneral):
    @staticmethod
    def peutcreer(request):
        """ Tout les utilisateurs peuvent faire une commande."""
        return POST(request) and request.user.is_authenticated

    def permissionspecial(self, request, view):
        return PermissionCommande.peutcreer(request) or DEL(request) or PUT(request)


    def permissionspecialobjet(self, request, view, obj):
        """ Seul le propriétaire a tout les accèss."""
        return obj.proprietaire == request.user


class PermissionEnseigne(PermissionGeneral):
    @staticmethod
    def moinsdetroisenseigne(utilisateur):
        nombre = 0
        for enseigne in Enseigne.objects.all():
            if Marque.possede(enseigne.marqueEnseigne, utilisateur):
                nombre += 1
                if nombre >= 3:
                    return False
        print(utilisateur.username, f" possède {nombre} enseigne")
        return True
        # return not request.user.is_staff

    @staticmethod
    def peutposter(request):
        """ Un propriétaire de marque avec moins de trois enseigne peut poster"""
        return (POST(request) and
                PermissionEnseigne.moinsdetroisenseigne(request.user))

    def permissionspecial(self, request, view):
        """ Les staff ont un accès complet et le propriétaire ont un accèss restreint"""
        return staffAll(request) or (Marque.estproprietaire(request.user) and ((DEL(request) or PUT(request)) or PermissionEnseigne.peutposter(request)))

    def permissionspecialobjet(self, request, view, obj):
        return  request.user.is_staff or Marque.possede(obj.marqueEnseigne, request.user)


class PermissionProduit(PermissionGeneral):
    @staticmethod
    def privilegeproducteur(request):
        """ Un utilisateur propriétaire d'une marque peut créer un produit."""
        return request.user in Marque.listeproprietaire() and request.method in ['POST', 'PUT', 'DELETE']

    def permissionspecial(self, request, view):
        return PUT(request) or PermissionProduit.privilegeproducteur(request) or DEL(request)

    @staticmethod
    def proprietairemarqueproduit(request, produit: Produits):
        """ Le propriétaire d'une marque à l'accès total à ses produits"""
        listeproprio = list(produit.marqueProduits.proprietaires.all())
        print(request.user.username)
        if request.user in listeproprio:
            return True
        return False

    @staticmethod
    def pasProduitPhare(produit):
        print()
        for enseigne in Enseigne.objects.all():
            if produit == enseigne.produitPhare:
                print(produit.nomProduits,': est un produit phare de ', enseigne.nomEnseigne,
                      " et ne peut donc pas etre suprimmer")
                return False
        return True

    @staticmethod
    def aeteComandee(produit):
        for commande in Commande.objects.all():
            if produit in list(commande.produits.all()):
                print(produit,' est présent dans une commande')
                return True
        return False

    @staticmethod
    def staffUpdate(request):
        return request.user.is_staff and PUT(request)

    def permissionspecialobjet(self, request, view, obj):
        """
        Le staff peut modifier.
        Le propriétaire a un accès complet sauf suppression de produit phare ou comandée
        """
        if PermissionProduit.staffUpdate(request):
            return True

        if PermissionProduit.proprietairemarqueproduit(request, obj):
            if request.method == 'DELETE':
                # Avant de suprimer un produit vérifier si il est un produit phare ou comandée
                return PermissionProduit.pasProduitPhare(obj) and not PermissionProduit.aeteComandee(obj)
            return True
        return False







