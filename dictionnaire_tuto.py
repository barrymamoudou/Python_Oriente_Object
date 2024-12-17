"""
exemple sur les dictionnaires
    syntaxe {'clet': 'valeur'}
    pour l'affiche
"""

#personne = { 'nom':'Mamoudou', 'age':25, 'taille':1.5}

# pour afficher le dict
#print(personne)
#pour afficher le nom dans un dict
"""print(personne['nom'])
print(personne['age'])"""
#si on veut modifier le champ nom dans le dict
#personne['nom']="barry"


#personne['Postes']='Developpeur'


#achats=('chocalat',"biscuits", "bonbon")

#personne['achats']=achats
"""print(personne)"""
"""for i in personne:
    print(f"Clet: {i} - valeur {personne[i]} ")"""

# ------------------------Partie 2 -------------------------------------------------------------------------------------

# imaginon que on a

personnes=[
    ('Mamoudou',25,1.7),
    ('Ramatoulaye',18,1.7),
    ('Oumou',25,1.7),
    ('ibrahima',24,1.7),
]

def obtenir_infos(nom, list):
    for i in list:
        if i[0]==nom:
            return i
    return None


infos=obtenir_infos("diallo",personnes)
#print(infos)

personnes_dic={
    "Mamoudou": (24,1.5),
    "oumou": (24,1.7),
}


#infos=personnes_dic["dfff"]
infos=personnes_dic.get("oumou")
if not infos:
    print("la cle n'existe pas ")
else:
    print(infos)


