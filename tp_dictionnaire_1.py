"""
              Exercice 1 : Manipulation de dictionnaires
              Créez un dictionnaire représentant une personne avec les informations suivantes : prénom, nom, âge, ville,
              profession.
              Ensuite, faites les opérations suivantes :
Accédez à l'âge de la personne.
              Ajoutez un numéro de téléphone.
              Changez le prénom de la personne.
Affichez toutes les informations sous forme de paires clé-valeur.
"""
"""nom_personne={ "prenom":"Mamoudou","nom":"barry","age":27,"ville":"conakry", "profession":"informaticien"}

#  Accédez à l'âge de la personne.

age_personne=nom_personne["age"]

print(age_personne)

#Ajoutez un numéro de téléphone.

nom_personne['telephone'] = 624201460

print(nom_personne)

#Changez le prénom de la personne ...

nom_personne['prenom']="kitcha sidibe"

print(nom_personne)

for cle,valeur in nom_personne.items():
    print(f"la cle - {cle} et la valeur - {valeur}")"""

"""
Exercice 2 : Vérification de l'existence d'une clé
Créez un dictionnaire contenant les noms des étudiants comme clés et leurs notes comme valeurs. 
Vérifiez si un étudiant existe dans ce dictionnaire et affichez sa note si la clé existe.

notes = {
    "Alice": 15,
    "Bob": 18,
    "Clara": 12
}

nom_etudiant="Bob"

if nom_etudiant in notes:
    print(f"{nom_etudiant} a obtenu {notes[nom_etudiant]} de moyenne.")
else:
    print(f"{nom_etudiant} n'est pas dans la liste.")

"""

"""

4. TP : Gestion d'une bibliothèque
Imaginons que vous gérez une bibliothèque.
Vous devez créer un dictionnaire où chaque clé est le titre d'un livre, et chaque valeur est un sous-dictionnaire avec les informations suivantes :
auteur
année de publication
nombre de pages
disponible (True/False)
Objectifs :
Ajouter un livre à la bibliothèque.
Modifier le statut de disponibilité d’un livre.
Afficher la liste des livres disponibles.
Afficher les informations d’un livre donné.

"""

biblo={
    "Python pour les nuls": {
        "auteur": "John Smith",
        "année": 2020,
        "pages": 350,
        "disponible": True
    },
    "La science du futur": {
        "auteur": "Marie Curie",
        "année": 2019,
        "pages": 250,
        "disponible": False
    },
    "La science du c++": {
        "auteur": "Marie Curie",
        "année": 2018,
        "pages": 250,
        "disponible": False
    },
    "La science du Algo": {
        "auteur": "Mamoudou",
        "année": 2017,
        "pages": 260,
        "disponible": True
    }
}

#Ajouter un livre à la bibliothèque.
biblo["L'intelligence artificielle"] = {
    "auteur": "Alice Lemoine",
    "année": 2021,
    "pages": 400,
    "disponible": True
}

#Modifier le statut de disponibilité d’un livre.
biblo["L'intelligence artificielle"]["disponible"]=False



#Afficher la liste des livres disponibles.
print("-----Afficher les Livres Disponible--------")
for titre , infos in biblo.items():
    if infos['disponible']:
        print(f"titre - {titre}")

print()
print("----------------------------------------")
print()

#Afficher les informations d’un livre donné.

titre_recherche="La science du futur214"
if titre_recherche in biblo:
    afficher=biblo[titre_recherche]
    for cle, valeur in  afficher.items():
        print(f"la cle - {cle} et la valeur - {valeur}")









