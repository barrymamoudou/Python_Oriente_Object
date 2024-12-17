# Exercice sur les pizza

def afficher(collection):
    nbr_pizza = len(collection)
    # ce une partir qui verifier si l'utilisateur entre rien pour le pizza
    if nbr_pizza == 0:
        print("AUCUN PIZZA")
        return True
    print(f"----------LISTE DES PIZZAS ({nbr_pizza}) --------------")
    for i in collection:
        print(i)
    print()
    print("Premiere pizza :" + collection[0])
    print("Premiere pizza :" + collection[-1])


# la fonction qui permet d'ajoute le pizza dans la collection
def ajoute_pizza(collection):
    """
        Ajoute une pizza à la collection si elle n'existe pas déjà.
    """
    p = input("Entre le Nom de Pizza :" )
    #on va utiliser les lower() et upper() pour mettre en minuscule et majuscule
    if p.lower() in collection.lower():
         print(f"La pizza '{p}' est déjà dans la collection.")
    else:
        collection.append(p)
        print(f"La pizza '{p}' a été ajoutée à la collection.")


"""def existe_pizza(e, collection):
         #Vérifie si l'élément e existe dans la collection. Retourne l'élément s'il existe, sinon retourne None. 
    for i in collection:
        if i==e:
            return True
    return False"""


# la fonction qui permet de verifier
pizza = ["4 formage", "vegetarien", "venise"]
vide = ""
ajoute_pizza(pizza)
afficher(pizza)
