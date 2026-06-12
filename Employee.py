from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Classe de base abstraite représentant un employé.
    """
    _matricule: int
    _nom: str
    _prenom: str
    _date_naissance: str

    def __init__(self, matricule, nom, prenom, date_naissance):
        self._matricule = matricule
        self._nom = nom
        self._prenom = prenom
        self._date_naissance = date_naissance

    def __str__(self):
        return f"{self._prenom} {self._nom} (Matricule: {self._matricule}, Né le : {self._date_naissance})"

    @abstractmethod
    def get_salaire(self):
        """Méthode abstraite pour calculer le salaire de l'employé."""
        pass

class Ouvrier(Employee):
    """
    Représente un ouvrier avec un salaire basé sur l'ancienneté.
    """
    __anciennete: int

    def __init__(self, anciennete, matricule, nom, prenom, date_naissance):
        super().__init__(matricule, nom, prenom, date_naissance)
        self.__anciennete = anciennete

    def get_salaire(self):
        return 1700 + (self.__anciennete * 100)

    def __str__(self):
        return super().__str__() + f", Salaire: {self.get_salaire():.2f}$"

class Cadre(Employee):
    """
    Représente un cadre avec un salaire basé sur un indice.
    """
    __indice: int

    def __init__(self, indice, matricule, nom, prenom, date_naissance):
        super().__init__(matricule, nom, prenom, date_naissance)
        self.__indice = indice

    def get_salaire(self):
        salaires = {1: 3000, 2: 4000, 3: 5000}
        return salaires.get(self.__indice, 6000)

    def __str__(self):
        return super().__str__() + f", Salaire: {self.get_salaire():.2f}$"

# ----------------- Programme principal -----------------

em1 = Ouvrier(2, 2845, "Jean", "Dupont", "1990-07-09")
em2 = Cadre(1, 3424, "Claire", "Dusseau", "1999-08-09")
em3 = Cadre(3, 3456, "Celine", "Jacques", "1995-07-07")

print("--- Gestion des Employés ---")
print(em1)
print(em2)
print(em3)
