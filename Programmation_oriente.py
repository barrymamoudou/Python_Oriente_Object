"""
    1-Self les objects
"""
"""
  class Personne:
    def __int__(self,nom : str, age:int):
        self.nom=nom
        self.age = age
        print("Contructeur personne " + nom)
    def Sepresenter(self):
        print(" Bonjour je m'appelle " + self.nom + ", j'ai "+ str(self.age) + "ans")
persone1= Personne("Mamoudou",25)
persone2= Personne("Mamoudou",25)
persone1.Sepresenter()
  on creer une fonction qui permet de dire si une personne est mineur ou majeur 
  
  la sceance pour mettre les donnes en abscence 
    on charge tout agents et on parcour si on trouver un agent on checkd il es presence ou non trouver alors i
    on veut aussi voir si il majeur on afficher ou si il mineur on afficher sur l'ecran 
"""
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        print("Contructeur personne " + nom)

    def Sepresenter(self):
        print(" Bonjour je  m'appelle " + self.nom + ", j'ai " + str(self.age) + "ans")
        print("La fonction", self.EstMajeur())

    def EstMajeur(self):
        if self.age >=18:
            return True
        return False
persone1 = Personne("Mamoudou", 25)
persone2 = Personne("binta", 15)
persone1.Sepresenter()
persone2.Sepresenter()



