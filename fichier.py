import os
"""
os.getlogin : renvoi les donnes de l'utilisateur connecte
2- 3.1.2 La méthode os.mkdir()

renvoi le repertoire actuel os.getcwd()

reper_toir=os.getcwd()
print(reper_toir)
"""

"""users=os.getlogin()
print(users)"""
"""os.mkdir("Bureau:/myFolder")"""

fichier_path='C:\\Users\\victus\\Desktop\\myFichier.txt'

if os.path.exists(fichier_path):
    with open(fichier_path,'r') as f:
        contenu = f.read()
else:
    print("Le fichier n'existe pas à l'emplacement spécifié.")
