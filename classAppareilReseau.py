class AppareilReseau:
    _ip: str # Changed type hint from int to str for IP address
    _nom: str
    _connecte: bool

    def __init__(self,ip,nom):
        self._ip = ip
        self._nom = nom
        self._connecte = False

    def connecter(self):
        self._connecte = True

    def deconnecter(self):
        self._connecte = False

    def afficher_info(self):
        return f"Nom: {self._nom}\nIP:{self._ip}\nConnecte: {self._connecte}"

class Serveur(AppareilReseau):
    def __init__(self,ip,nom,systeme_exploitation,nb_services):
        super().__init__(ip,nom)
        self.__systeme_exploitation = systeme_exploitation
        self.__nb_services = nb_services

    """Methodes"""
    def get_systeme_exploitation(self):
        return self.__systeme_exploitation

    def get_nb_services(self):
        return self.__nb_services

    def demarrer_services_exploitation(self):
        print("Demarrage des services de systeme d'exploitation")

    def afficher_info(self):
        return super().afficher_info() + f"\nSysteme exploitation: {self.__systeme_exploitation}\nnb_services: {self.__nb_services}"

class Routeur(AppareilReseau):
    def __init__(self,ip,nom,nb_interfaces,firmware_version):
        super().__init__(ip,nom)
        self.__nb_interfaces = nb_interfaces
        self.__firmware_version = firmware_version

    def get_nb_interfaces(self):
        return self.__nb_interfaces

    def get_firmware_version(self):
        return self.__firmware_version

    def redemarrer(self):
        print("Redemarrage du Routeur")

    def afficher_info(self):
        return super().afficher_info() + f"\nInterfaces: {self.__nb_interfaces}\nfirmware: {self.__firmware_version}"

"""Programme principal"""

Serveur1 = Serveur("192.168.1.10","Serveur 1","Windows",10)
Routeur1 = Routeur("192.168.1.11","Routeur 1",5,1.9)

Serveur1.connecter()
print(Serveur1.afficher_info())
print()
Routeur1.connecter()
print(Routeur1.afficher_info())
print()
Serveur1.demarrer_services_exploitation()
print(Serveur1.afficher_info())
print()
Routeur1.redemarrer()
print(Routeur1.afficher_info())
print()
appareils = [Serveur1,Routeur1]
for appareil in appareils:
    print(appareil.afficher_info())
    print()
