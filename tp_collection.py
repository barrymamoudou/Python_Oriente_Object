#----------Collection-----------------------------
# tableau:array mais avec importation, tuples, Liste
#Tuples : immutable ont ne peut pas les modifier ni ajoute ni supprimer on les reconnais a partir des()
#List[] : sont mutable ont peut ajouter/supprimer sont des donnes modifiable

#-------------------------Tuples-----------------------------------------------------

personnes=("barry","diallo","elhadj","sow")

#print(len(personne))
#print(personne)

#for i in range(0,len(personne)) :
#    print(personne[i])

# -------------------------List-----------------------------------------------------
"""
personnes=["barry","diallo","elhadj","sow"]

nouvelle_personn="david"

#print(personnes)

personnes.append(nouvelle_personn)
del personnes[1]
print(personnes)


def afficher_informations(c):
     for i in c:
        print(i)

def modifier_information(a):
    a[0]=10

test=[1,2,3,4]
print(test)
modifier_information(test)
print(test)"""

# -------------------------Fonctions Et Tuples -----------------------------------------------------
#Utilisation le mot return

"""def obtenir_informations():
    return "Moud",12,1.6


def afficher_information(nom,age,taille):
    print(f"Informations : Nom: {nom}, age : {age}, taille : {taille}")
infos=obtenir_informations()
afficher_information(*infos) #unpack tuple

print(infos)
print(*infos)""" #quivaut a ecrire infos[0], infos[1],infos[2] eq
#nom,age,taille=obtenir_informations()
#afficher_information(nom,age,taille)

# -------------------------Slices -------------------------------------------------------------------

"""personne=("barry","diallo","elhadj","sow")"""

# -------------------------Exercice sur les List -----------------------------------------------------

"""noms=[]

while True:
    nom=input("Nom de la personne : ")
    if nom =='':
        break
    noms.append(nom)

print("Afficher des Resultats")
print(noms)
print()
print("Nom des Personnes")
noms.sort()
for nom in noms :
    print(nom)"""

# -------------------------Exercice Algorithme -----------------------------------------------------
# LISTE-ALGO = > VALEUR LA PLUS PETITE
nom_chauffeur_km=['barry',"diallo","balde","camara","sylla","bangoura","sylvie"]
distance_chauffeur_km=[1.5,2.2,0.4,0.9,7.1,1.1,0.6]

index_min=0

distance_min=distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)) :
    distance= distance_chauffeur_km[i]
    if distance < distance_min :
        distance_min=distance
        index_min=i


print("Distance minimale:", distance_min)
print("Index chauffeur", index_min)
print("Nom de chauffeur ", nom_chauffeur_km[index_min])
