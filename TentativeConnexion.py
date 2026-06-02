class TentativeConnexion:
    utilisateur: str
    ip: str
    statut: str

    def __init__(self,utilisateur,ip,statut):
        self.utilisateur = utilisateur
        self.ip = ip
        self.statut = statut

    def __str__(self):
        return f"Tentative de connexion: utilisateur={self.utilisateur} IP={self.ip} Status={self.statut}"

    def __eq__(self,other):
        return self.ip == other.ip and self.utilisateur == other.utilisateur


t1=TentativeConnexion("admin","192.168.1.20","Echec")
t2=TentativeConnexion("admin","192.168.1.20","Succes")
t3=TentativeConnexion("user","192.168.1.30","Echec")

print(t1)
print(t2)
print(t3)

if t1 == t2:
    print("t1 == t2 ? True")
else:
    print("t1 == t2 ? False")

if t1 == t3:
    print("t1 == t3 ? True")
else:
    print("t1 == t3 ? False")
