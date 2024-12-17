
def pose_question(question,r1,r2,r3,r4,choix_bonne_reponse):
    global score
    print("QUESTION")
    print(" " + question)
    print(" (a)",r1)
    print(" (b)", r2)
    print(" (c)",r3)
    print(" (d)",r4)

    reponse = input("Votre reponse : ")
    #reponse_correct=False
    if reponse == choix_bonne_reponse:
        print("Bonne reponse")
        score+=1
       # reponse_correct = True
    else:
        print("Mauvaise réponse")
    #return reponse_correct

score=0
pose_question("Quelle est la capitale de la france ?","Marseille","Nice","Paris","Nantes","c")
pose_question("Quelle est la capitale de la Italie ?","Rome","Venise","Pise","Florence","a")

print("Score Final :",score)