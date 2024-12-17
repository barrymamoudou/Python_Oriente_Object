from zipfile import ZipFile


with ZipFile('nom_fichier', 'r') as zp_ocb:
    zp_ocb.extractall()


print(zp_ocb.namelist())
"""
1.Gestion d'un carnet d'adresses
Vous devez créer un programme qui gère un carnet d'adresses sous forme de dictionnaire,
où les clés sont les noms des personnes et les valeurs sont leurs informations de contact (numéro de téléphone, email).
Vous devez implémenter les fonctionnalités suivantes :
adress_carnet={}
{telephone: 624201460, email:mamaoudoubarry@gamil}

-Ajouter une nouvelle personne avec ses coordonnées.
-Modifier les coordonnées d'une personne existante.
-Supprimer une personne du carnet.
-Afficher les coordonnées d'une personne donnée.
-Afficher toutes les personnes du carnet.




"""

"""  
carnet_adrees={}

#la fonction qui ajouter un carnet
def ajouter_carnet(nom,telephone,email):
    carnet_adrees[nom] = {'telephone': telephone, 'email': email}

# la fonction qui permet de modifier
def modifier_personne(nom,telephone=None,email=None):
    if nom in carnet_adrees:
        if telephone:
            carnet_adrees[nom]['telephone']=telephone
        if email :
            carnet_adrees[nom]['email'] = email
    else :
        print("Cette personne n'existe pas.")

#supprimer une personne
def supprimer_personne(nom):
    if nom in carnet_adrees:
        del carnet_adrees[nom]
    else:
        print("Cette personne n'existe pas.")

def afficher_tous(nom):
    if nom in carnet_adrees:
        print(f"{nom}: {carnet_adrees[nom]}")
    else:
        print("Cette personne n'existe pas.")
"""



