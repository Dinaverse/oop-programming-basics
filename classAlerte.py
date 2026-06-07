class Alerte:
    _id: int
    _source: str
    _niveau: str
    _active: bool

    def __init__(self, id: int, source: str, niveau: str):
        self._id = id
        self._source = source
        self._niveau = niveau
        self._active = True

    def get_niveau(self):
        return self._niveau

    def desactiver(self):
        self._active = False
        print("Alerte désactivée")

    def afficher_info(self):
        return f"ID: {self._id}\nSource: {self._source}\nNiveau: {self._niveau}\nActive: {self._active}"


class AlerteIntrusion(Alerte):
    __ip: str
    __nb_tentative: int

    def __init__(self, id: int, source: str, niveau: str, ip: str, nb_tentative: int):
        super().__init__(id, source, niveau)
        self.__ip = ip
        self.__nb_tentative = nb_tentative

    def analyser_risque(self):
        if self.__nb_tentative > 5:
            print("Risque élevé")
        else:
            print("Tentatives faibles")

    def afficher_info(self):
        return super().afficher_info() + f"\nIP: {self.__ip}\nTentatives: {self.__nb_tentative}"

class AlerteMalware(Alerte):
    def __init__(self, id: int, source: str, niveau: str, type_malware: str, fichier_infecte: str):
        super().__init__(id, source, niveau)
        self.__type_malware = type_malware
        self.__fichier_infecte = fichier_infecte

    def isoler_machine(self):
        print("La machine est isolée du reseau")

    def afficher_info(self):
        return super().afficher_info() + f"\nMalware: {self.__type_malware}\nFichier: {self.__fichier_infecte}"

a1 = AlerteIntrusion(101, "Firewall", "Élevé", "198.168.32.65", 59)
a2 = AlerteMalware(102,"Antivirus","Critique","Ransomware","virus.exe")
print(a1.afficher_info())
print()
print(a2.afficher_info())
print()
a1.analyser_risque()
a2.isoler_machine()

alertes=[a1,a2]

for alerte in alertes:

    print(alerte.afficher_info())

    print()
