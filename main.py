
essaie = 3
i = 0
annee = ['1994','1998','2002','2006','2010','2014','2018']
pays = ['bresil', 'france', 'bresil', 'italie', 'espagne', 'allemagne', 'france']

while essaie > 0 and i < len(annee):
    print("Essaie " + str(essaie) +"/3")
    print("Question " + str(i + 1) +"/7: Quelle equipe a gagne la coupe du monde de "+ annee[i]+ "?")
    reponse = input()

    while reponse == None or len(reponse) == 0:
        print("Veuillez entrer une reponse valide.")
        reponse = input() 

    if(reponse.lower() != pays[i]):
        essaie -= 1
        print("Reponse incorrect. Vous avez " + str(essaie) + " essaie restant. \n\n")
    else:    
        print("Correct! \n\n")
        i += 1

if(essaie == 0):
    print("Nous n'avez pas reussi a finir le questionnaire. Reesayer une autre fois.")
else:
    print("Bravo!! Vous avez reussi a finir le quiz avec "+ str(3-essaie) + " erreur(s).")
