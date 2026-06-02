class Compte:
    # Definition des attributs de la classe Compte
    numero_compte: int
    nom_titulaire: str
    solde : float

    # Constructeur qui initialise les trois attributs numero_compte, nom_titulaire, et solde
    def __init__(self, numero_compte, nom_titulaire, solde):
        self.numero_compte = numero_compte
        self.nom_titulaire = nom_titulaire
        self.solde = float(solde)

    def afficher_compte(self):
        print(f"Numero de compte:{self.numero_compte}\nTitulaire:{self.nom_titulaire}\nSolde actuel:{self.solde:.2f}$\n")

    # Methodes

    def crediter(self,montant:float):
        self.solde = self.solde + montant

    def debiter(self,montant:float):

        if montant > self.solde:
            print("Erreur: Solde insuffisant pour le retrait!")
        else:
            self.solde = self.solde - montant

    #-----------------Programme principale------------------

Compte1 =Compte("101","Alice Dupont","500")
Compte2 =Compte("102","Bob Martin","1200")

Compte1.afficher_compte()
print("---------------------")
Compte2.afficher_compte()

print("Depot de 150$ sur le compte 1")
Compte1.crediter(150)
Compte1.afficher_compte()

print("Retrait de 100$ sur le compte 1")
Compte1.debiter(100)
Compte1.afficher_compte()

print("Tentative de retrait de 1000$ sur le compte 1")
Compte1.debiter(1000)
Compte1.afficher_compte()

print("Retrait de 300$ sur le compte 2")
Compte2.debiter(300)
Compte2.afficher_compte()