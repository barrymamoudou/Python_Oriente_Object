
"""
recuperer_et_afficher_infos_information()
qui afficher des input et print()
    ->recuperer_infos_personel
    ->afficher_infos_personne
        ->estMajeur()
"""
def est_majeur(age):
    if age <= 0 :
        return False
    if age >=10 :
        return True
def recuperer_infos_personel(numero_personne):
    nom_personel = input("Nom de la personnel " + str(numero_personne) + " :")
    while True :
        age_personel = input("Age de la personne :" + str(numero_personne) + " :")
        try:
            age_converti=int(age_personel)
            break
        except ValueError :
            print("Erreur : Veuillez entrer une valeur numérique valide pour l'âge.")
    return nom_personel, age_converti

def afficher_infos_personne(nom, age,numero_personne):
    print("La personne ", numero_personne, "est", nom, "son age est", age, "ans")
    print("le comporte", len(nom), "lettres")
    if est_majeur(age) :
        print("il est majeur")
    else:
        print("il est mineur")
def recuperer_et_afficher_infos_information(numero_personne):
    nom,age=recuperer_infos_personel(numero_personne)
    afficher_infos_personne(nom, age,numero_personne)
    """print("La personne ",numero_personne,"est",nom, "son age est", age, "ans")
    print("le comporte", len(nom), "lettres")"""
nbr_constant=2
for i in range(nbr_constant):
    recuperer_et_afficher_infos_information(i+1)
afficher_infos_personne("005","barry",17)




