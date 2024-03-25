'''''''''
**Jeu du plus ou mois !**  
L'ordinateur tire un nombre entier au hasard entre 30 et 100.  
L'utilisateur doit le trouver et pour cela il propose des valeurs.   
L'ordinateur indique pour chaque valeur proposée si elle est trop petite, trop grande ou s'il a trouvé !  
'''''''''
from random import randint

class PlusOuMoins:
    def __init__(self):
        self.NOMBRE_DE_PARTIE_JOUE = 0
        self.NOMBRE_TOTAL_ESSAIS = 0
        self.NOMBRE_ECHEC = 0

    def play(self):
        self.NOMBRE_DE_PARTIE_JOUE += 1
        NUMERO_ALEATOIRE = randint(30, 100)
        ESSAIS = 0

        while True:
            ESSAIS += 1
            UTILISATEUR = self.get_user_input(ESSAIS)
            if UTILISATEUR == NUMERO_ALEATOIRE:
                print(f"Bravo, vous avez trouvé le bon nombre ({NUMERO_ALEATOIRE}) en {ESSAIS} essais")
                break
            elif UTILISATEUR < NUMERO_ALEATOIRE:
                print("C'est plus !")
            else:
                print("C'est moins !")
            if ESSAIS == 5:
                print('Attention, vous êtes à votre 5ème essai !')
            if ESSAIS == 10:
                print("Dommage, vous avez perdu. Le nombre à trouver était :", NUMERO_ALEATOIRE)
                self.NOMBRE_ECHEC += 1
                break
        self.NOMBRE_TOTAL_ESSAIS += ESSAIS

    def get_user_input(self, ESSAIS):
        while True:
            try:
                UTILISATEUR = int(input(f"Tentative numéro {ESSAIS}: Sélectionnez un nombre entre 30 et 100 : "))
                if 30 <= UTILISATEUR <= 100:
                    return UTILISATEUR
                else:
                    print("Le nombre doit être compris entre 30 et 100.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

    def run(self):
        while True:
            NOUVELLE_PARTIE = input("Voulez-vous faire une partie ? (O ou N)").upper()
            if NOUVELLE_PARTIE == "N":
                self.save_results()
                break
            elif NOUVELLE_PARTIE == "O":
                self.play()
            else:
                print("Je n'ai pas compris")

    def save_results(self):
        with open("Resultats_Juste_Prix.txt", "w") as fichier:
            TAUX_REUSSITE = ((self.NOMBRE_DE_PARTIE_JOUE - self.NOMBRE_ECHEC) * 100) / self.NOMBRE_DE_PARTIE_JOUE if self.NOMBRE_DE_PARTIE_JOUE != 0 else 0
            fichier.write(f"\nNb de parties: {self.NOMBRE_DE_PARTIE_JOUE} | Nb essais moyens: {self.NOMBRE_TOTAL_ESSAIS / self.NOMBRE_DE_PARTIE_JOUE} | Taux réussite: {TAUX_REUSSITE}")

if __name__ == "__main__":
    game = PlusOuMoins()
    game.run()
