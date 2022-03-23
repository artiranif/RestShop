Sommaire:
- Avant-propos
- Introduction
- Installation
- Règle de gestion
- Règle non annoncée

AVANT-PROPOS:
Il est conseillé de lire l'installation(requirement) et Règle de gestion (Règle spontannée), toute fois le projet devrait être facilement utilisable et des documentations sont présent dans le code. 

INTRODUCTION:
Ce projet simule un magasin virtuel, mais l'aspect front-end a été laisser pour favoriser le dévellopement car il s'agit là de mon premier projet sous RestFramework. 

INSTALLATION:
Utiliser la même version des logiciels est le plus recommandé, entre parenthèse sont les versions que j'ai utilisé.

Requirement:
Odoo ou les composants suivant:
- python 3.6-3.8 (3.8.5)
- django (3.1)
- restframework (3.12.4)
- système d'exploitation minimal: Window 7 SP1

LANCEMENT:
- Utiliser le fichier bat ou lancer le serveur vous même.
- Vous aurez directement accèss à l'api de restframework.

Utilisation:
- Vous pouvez vous connectez avec les utilisateurs fournies ou créer de nouveau.
- Les liens vers les modules sont accéssibles sur l'index du site, et vous pouvez cliquer sur un élément y accéder.

REGLE DE GESTION:
- Toutes les informations sont accécibles, même sans authentification
- Une Marque ne peut être créer et contrôler que par un Staff
- Une Enseigne peut être créer par un propriétaire de Marque à la limite de trois ou un Staff. Et contrôler par son propriétaire de Marque ou un Staff.
- Un Produit peut être créer que par un propriétaire de Marque.
- Une Commande peut être faite par un utilisateur.
- Seul l'utilisateur à le plein contrôle sur sa commande.

Règle spontannée:
- Une Marque peut avoir plusieur propriétaires (présence de 's') et un propriétaire peut avoir plusieurs marques.
- Un propriétaire ne peut qu'utiliser sa ou ses marques.
- INCONNUS: soit une commande est supprimer après livraison et stoker dans une autre table, et donc est supprimer soit par le client(peut probable) ou le staff(non annoncée dans le sujet) OU
soit les commandes sont juste créer.
Nous utiliserons cette dernière hypothèse dans le doute.
