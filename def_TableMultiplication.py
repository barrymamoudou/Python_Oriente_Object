# EXERCICE FONCTIONS

# Tables de multiplications

# 1x 4 = 4

# 2x 4 = 8

# 3x 4 = 12

# ....

# 10x 4 = 40
#

#afficher_table_multiplication(n)

# min / max

# erreur : si min > max

def afficher_table_multiplication(n, min, max):
    if min > max :
        print("Erreur ")
    return
    min=1
    max=10
    #au niveau du boucle le max est execlusive
    for i in range(min, max+1):
        print(i, "x", n, "=",i*n )
print("Le programme affiche la table ")
afficher_table_multiplication(5,2,1)




