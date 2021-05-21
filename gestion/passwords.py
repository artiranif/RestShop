from random import randrange

""" Génère un mot de passe."""
mot = ""
for i in range(20):
    mot += chr(randrange(80,100))
print(mot)
input('Votre mot de passe est prêt à être copier !!!')