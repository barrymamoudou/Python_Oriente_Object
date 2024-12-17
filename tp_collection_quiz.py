#

def demande_un_nombre(min, max):
    reponse_str = input("Votre reponse (entre "+str (min )+" et "+str(max)+ ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("Erreur vous devez entre un nombre compris "+min, "et" , +max)
    except :
        print("Erreur : Entre des Chiffres ")
    return demande_un_nombre(min, max)

#title_question=question[0]
#choix=question[1]
#choix_bonne_reponse=[2]


def pose_question(question):

    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION")
    print(" " + question[0])
    for i in range(len(choix)):
        print(" ",i+1,"-",choix[i])

    reponse_int=demande_un_nombre(1, len(choix))
    #reponse_correct=False

    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne reponse")
        score+=1
       #reponse_correct = True
    else:
        print("Mauvaise réponse")
    #return reponse_correct

score=0

question1=("Quelle est la capitale de la france ?",("Marseille","Nice","Paris","Nantes","Lille"),"Paris")
question2=("Quelle est la capitale de la Italie ?",("Rome","Venise","Pise","Florence"),"Rome")
pose_question(question1)
pose_question(question2)
print("------------------------------------Resultat-----------------------------------------")
print("Score Final :",score)


"""
    questionaire []
        question
        title_question=""
        reponse=("marseille","paris")
        bon_reponse="paris"
        
        
        on va creer un fonction qui lance le questionnaire et on boucle dedans ensuite on 
        verifier si le questionnaire est vrai on incremente le score mais on doit declare le score

"""