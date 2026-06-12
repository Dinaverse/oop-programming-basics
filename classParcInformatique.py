from abc import ABC, abstractmethod

class Equipement(ABC):
    """
    Classe de base abstraite représentant un équipement informatique.
    """
    _nom: str
    _numero: str
    _marque: str
    _est_allume: bool

    def __init__(self, nom, numero, marque, est_allume):
        self._nom = nom
        self._numero = numero
        self._marque = marque
        self._est_allume = est_allume

    @abstractmethod
    def executer_tache(self):
        """Méthode abstraite pour exécuter une tâche spécifique."""
        pass

    def effectuer_maintenance(self):
        """Méthode de base pour la maintenance (peut être surchargée)."""
        pass

    def __str__(self):
        etat = "Allumé" if self._est_allume else "Éteint"
        return f"Nom: {self._nom} | No: {self._numero} | Marque: {self._marque} | État: {etat}"


class Ordinateur(Equipement):
    """
    Représente un ordinateur avec une capacité de RAM spécifique.
    """
    _capacite_ram: int

    def __init__(self, nom, numero, marque, est_allume, capacite_ram):
        super().__init__(nom, numero, marque, est_allume)
        self._capacite_ram = capacite_ram

    def executer_tache(self):
        return f"➤ [Ordinateur {self._nom}] Exécution d'un programme avec {self._capacite_ram} Go de RAM."

    def effectuer_maintenance(self):
        return f"➤ [Ordinateur {self._nom}] Nettoyage du disque et mise à jour de l'antivirus."

    def __str__(self):
        return super().__str__() + f" | RAM: {self._capacite_ram} Go"


class Imprimante(Equipement):
    """
    Représente une imprimante avec une vitesse d'impression.
    """
    _vitesse_impression: int

    def __init__(self, nom, numero, marque, est_allume, vitesse_impression):
        super().__init__(nom, numero, marque, est_allume)
        self._vitesse_impression = vitesse_impression

    def executer_tache(self):
        return f"➤ [Imprimante {self._nom}] Impression à {self._vitesse_impression} pages/minute."

    def effectuer_maintenance(self):
        return f"➤ [Imprimante {self._nom}] Vérification des cartouches et calibrage des têtes."

    def __str__(self):
        return super().__str__() + f" | Vitesse: {self._vitesse_impression} ppm"


class Serveur(Equipement):
    """
    Représente un serveur gérant un certain nombre d'utilisateurs.
    """
    _nombre_utilisateurs: int

    def __init__(self, nom, numero, marque, est_allume, nombre_utilisateurs):
        super().__init__(nom, numero, marque, est_allume)
        self._nombre_utilisateurs = nombre_utilisateurs

    def executer_tache(self):
        return f"➤ [{self._nom}] Traitement de requêtes pour {self._nombre_utilisateurs} utilisateurs."

    def effectuer_maintenance(self):
        return f"➤ [{self._nom}] Sauvegarde des données et redémarrage sécurisé."

    def __str__(self):
        return super().__str__() + f" | Utilisateurs: {self._nombre_utilisateurs}"


class ParcInformatique:
    """
    Classe gérant un ensemble d'équipements informatiques (Composition).
    """
    _equipments: list

    def __init__(self):
        self._equipments = []

    def ajouter_equipement(self, e: Equipement):
        self._equipments.append(e)

    def executer_toutes_taches(self):
        print("\n--- Exécution de toutes les tâches ---")
        for e in self._equipments:
            print(e.executer_tache())

    def maintenir_le_parc(self):
        print("\n--- Maintenance du Parc ---")
        for e in self._equipments:
            print(e.effectuer_maintenance())

    def afficher_equipments(self):
        print("\nInventaire du Parc Informatique :")
        
        print("\n[Ordinateurs]")
        for e in self._equipments:
            if isinstance(e, Ordinateur):
                print(e)

        print("\n[Imprimantes]")
        for e in self._equipments:
            if isinstance(e, Imprimante):
                print(e)

        print("\n[Serveurs]")
        for e in self._equipments:
            if isinstance(e, Serveur):
                print(e)


# ----------------- Programme Principal -----------------

parc = ParcInformatique()

# Création des objets
O1 = Ordinateur("Dell XPS", "101", "Dell", False, 16)
O2 = Ordinateur("MacBook Pro", "102", "Apple", False, 32)
Imp1 = Imprimante("HP LaserJet", "201", "HP", True, 30)
Imp2 = Imprimante("Canon Pixma", "202", "Canon", False, 20)
Ser1 = Serveur("Serveur-1", "301", "IBM", True, 150)
Ser2 = Serveur("Serveur-2", "302", "Dell", False, 250)

# Ajout au parc
parc.ajouter_equipement(O1)
parc.ajouter_equipement(O2)
parc.ajouter_equipement(Imp1)
parc.ajouter_equipement(Imp2)
parc.ajouter_equipement(Ser1)
parc.ajouter_equipement(Ser2)

# Affichage et exécution
parc.afficher_equipments()
parc.executer_toutes_taches()
parc.maintenir_le_parc()
