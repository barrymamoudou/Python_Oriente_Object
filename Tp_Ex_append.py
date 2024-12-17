"""
-les fonctionnalite de trie,
    sort()=> cest un object inplace,sorted()=> cest n'est pas un object inplace
    ,min , max , sum=> fait le calcul des elements au cas si ces des string il fait le calcul des elements
     ,in=dedans() verifier si une valeur est requis dedans
     echange des elements de la liste est que [initial_valeur],[arrive_initial]=[arrive_initial],[initial_valeur]
     join()=> "-"
     split() =
    all : renvoi tous si ces vrai
    any : renvoi au moins si une valeur est vrai dans la liste
    -Tester si une chaine contient des chiffres (isdigit, any)
        -any:
        -isdigit:


noms=["barry","diaby","diallo","balde", "mamoudou"]

age=[20,52,68,25,47,14]

noms.sort()

if "barry" in noms :
    print("Pressent")
else:
    print("absent")

    noms=["barry","diaby","diallo","balde", "mamoudou",'moussa']

noms[1],noms[5],noms[0], noms[4]=noms[5], noms[1],noms[4], noms[0]

"""

noms = ["Mamoudou", "Mamadou", 'AMINATA', 'Ibrahima']
s=0
for nom in noms:
    s+=len(nom)
    print("le nombre de caractere",s)


