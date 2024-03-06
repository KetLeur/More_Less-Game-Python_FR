'''''''''
**Jeu du plus ou mois !**  
L'ordinateur tire un nombre entier au hasard entre 0 et 100.  
L'utilisateur doit le trouver et pour cela il propose des valeurs.   
L'ordinateur indique pour chaque valeur proposée si elle est trop petite, trop grande ou s'il a trouvé !  
'''''''''

# Import des modules
from random import randint
nbpartie=0
totessaie=0
echec=0
fin=0

def play():
    global num, essais, totessaie, echec, nbpartie
    # Variable pour le jeu
    num = randint(30,100)
    essais = 1

    # Entrée utilisateur
    print("Tentative numéro :", essais)
    user = int(input("Selectionnez un nombre entre 30 et 100 : "))

    # Noyau du jeu qui permet de dire si supérieur ou inférieur
    while user != num:
        if user < num:
            essais=essais+1
            print("C'est plus !")
        else:
            print("C'est moins !")
            essais=essais+1
        # Nouvelle entrée utilisateur
        if essais==5:
            print('Attention, vous êtes à votre 5ème éssai !')
        print("Tentative numéro :", essais)
        if essais==11:
            break
        user = int(input("Selectionnez un nombre entre 30 et 100 : "))

    # Résultat
    totessaie=totessaie+essais
    if essais<11:
        print("Bravo, vous avez trouvé le bon nombre (",num,") en ", essais," essais")
    else:
        echec=+1
        print("Dommage, vous avez perdu. Le nombre à trouver était :", num)
def function_doyouwantplay():
    global doyouwantplay
    doyouwantplay=input("Voulez vous faire une partie ? : (O ou N)").upper()


while fin==0:
    function_doyouwantplay()
    if doyouwantplay=="O":
        nbpartie=+1
        play()
    elif doyouwantplay=="N":
        fin=1
        fichier = open("Python/Dev/Resultats_Juste_Prix.txt", "a")
        fichier.write("\nNb de parties  Nb essais moy   Taux reussite")
        taux=((nbpartie-echec)*100)/nbpartie
        result="\n",nbpartie,"   ",totessaie,"",taux,""
        fichier.write("\n"+str(nbpartie)+"------"+str(totessaie)+"------"+str(taux)+"")
        fichier.close()
    else:
        print("Je n'ai pas compris")
        function_doyouwantplay()

