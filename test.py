from random import randint

class PlusOuMoins:
    def __init__(self):
        self.nbpartie = 0
        self.totessaie = 0
        self.echec = 0

    def play(self):
        self.nbpartie += 1
        num = randint(30, 100)
        essais = 0

        while True:
            essais += 1
            user = self.get_user_input(essais)
            if user == num:
                print(f"Bravo, vous avez trouvé le bon nombre ({num}) en {essais} essais")
                break
            elif user < num:
                print("C'est plus !")
            else:
                print("C'est moins !")
            if essais == 5:
                print('Attention, vous êtes à votre 5ème essai !')
            if essais == 10:
                print("Dommage, vous avez perdu. Le nombre à trouver était :", num)
                self.echec += 1
                break
        self.totessaie += essais

    def get_user_input(self, essais):
        while True:
            try:
                user = int(input(f"Tentative numéro {essais}: Sélectionnez un nombre entre 30 et 100 : "))
                if 30 <= user <= 100:
                    return user
                else:
                    print("Le nombre doit être compris entre 30 et 100.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

    def run(self):
        while True:
            doyouwantplay = input("Voulez-vous faire une partie ? (O ou N)").upper()
            if doyouwantplay == "N":
                self.save_results()
                break
            elif doyouwantplay == "O":
                self.play()
            else:
                print("Je n'ai pas compris")

    def save_results(self):
        with open("Resultats_Juste_Prix.txt", "w") as fichier:
            taux = ((self.nbpartie - self.echec) * 100) / self.nbpartie if self.nbpartie != 0 else 0
            fichier.write(f"\nNb de parties: {self.nbpartie} | Nb essais moyens: {self.totessaie / self.nbpartie} | Taux réussite: {taux}")

if __name__ == "__main__":
    game = PlusOuMoins()
    game.run()
