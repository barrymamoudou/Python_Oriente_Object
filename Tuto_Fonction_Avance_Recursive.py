#Python Fonction : Notions avances
#
#Fonction Recursives
"""
     imaginon une def attribute
"""
def nombre_aleatoire(min, max):
    reponse_utilisateur=input("entre un nombre qui est compris " +str(min)+ "et" +str(max) + ":")
    try:
        reponse_int=int(reponse_utilisateur)
        if not min  <= reponse_int <= max :
            print("alors vous devez rentre un nombre compris ", min ,"et", max)
            return nombre_aleatoire(min, max)
        return  reponse_int
    except :
        print(" alors vous devez rentre un nombre ")
        return nombre_aleatoire(min, max)

choix=nombre_aleatoire(1,5)
print(" Choix d'utilisateur ", choix)
