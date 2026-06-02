class AutoPilot:
   """
   Ce système intelligent analyse la situation du véhicule en temps réel

    Attributs :
    - distance (float) : Distance au prochain obstacle (en mètres)
    - vitesse (float) : Vitesse actuelle du véhicule (en m/s)
    """
   distance: float
   vitesse: float

   def __init__(self, distance: float, vitesse: float):
        self.distance = distance
        self.vitesse = vitesse

   def decider_action(self):
        """prendre une décision (freiner, ralentir ou continuer)"""
        if self.distance < 5:
            return "Freiner"
        elif self.distance <= 10:
            return "Ralentir"
        else:
            return "Continuer"

   def afficher_avertissement(self):
        """afficher un avertissement visuel"""
        if self.distance < 5:
            print("⚠️ DANGER")
        elif self.distance <= 10:
            print("⚠️ Prudence")

   def temps_avant_impact(self):
        """estimer le temps avant impact"""
        if self.vitesse > 0:
            return self.distance / self.vitesse
        elif self.vitesse == 0:
            return float ('inf')
        else:
            return None

   def mettre_a_jour(self, distance: float, vitesse: float):
       """Met à jour la distance et la vitesse de l'objet"""
       self.distance = distance
       self.vitesse = vitesse

   def ajuster_vitesse(self):
       """Réduit la vitesse de 2 m/s et affiche la nouvelle vitesse"""
       self.vitesse = self.vitesse - 2
       print(f"Nouvelle vitesse : {self.vitesse}m/s")

   def __str__(self):
        return f"distance: {self.distance}, vitesse: {self.vitesse}"

   def arreter(self):
        """Met la vitesse du véhicule à 0"""
        self.vitesse = 0
        print("Le véhicule est à l'arrêt.")

   def est_arrete(self):
        """Vérifie si le véhicule est à l'arrêt"""
        return self.vitesse == 0

   def vitesse_en_kmh(self):
        return f"{self.vitesse * 3.6} Km/h"

   def est_proche(self):
        """Vérifie si un obstacle est très proche (moins de 3 mètres)"""
        return self.distance < 3

   def securite_activee(self):
       """Affiche un message indiquant que l'assistance est en fonction"""
       print("Assistance à la conduite activée.")

   def simuler_freinage(self):
        """Simule un freinage en réduisant la vitesse de 5 m/s (sans descendre sous 0)"""
        self.vitesse -= 5
        if self.vitesse < 0:
            self.vitesse = 0
        return f"{self.vitesse} m/s"

#--------------------Programme Principale--------------------------------

v1= AutoPilot(7,20)
print(f"Creation d'un vehicule avec distance = {v1.distance}m et vitesse = {v1.vitesse}m/s")
print("")
print("Activation du systeme de securite")
v1.securite_activee()
print("")
print("Etat intial:")
print(f"Distance: {v1.distance}m")
print(f"Vitesse: {v1.vitesse}m/s")
print("")
print("Decision selon la distance :")
print(v1.decider_action())
print("")
print("Avertissement visuel :")
v1.afficher_avertissement()
print("")
print("Temps estimer avant impact :")
print(v1.temps_avant_impact())
print("")
print("Reduction de la vitesse de 2 m/s :")
v1.ajuster_vitesse()
print(f"Distance: {v1.distance}m")
print(f"Vitesse: {v1.vitesse}m/s")
print("")
print(f"Mise a jour des donnees (distance = 5, vitesse = 12)")
v1.mettre_a_jour(5, 12)
print(f"Distance: {v1.distance}m")
print(f"Vitesse: {v1.vitesse}m/s")
print("")
print("Simulation de freinage (reduction 5 m/s) :")
print(f"freinage applique. Vitesse actuelle :{v1.simuler_freinage()}")
print("")
print("Verifie si le vehicule est arrete :")
print(f"Est arrete ?{v1.est_arrete()}")
print("")
print(f"Conversion de la vitesse en Km/h :\nVitesse actuelle en Km/h : {v1.vitesse_en_kmh()}")
print("")
print(f"Verifie si un obstacle est tres proche :\nObstacle tres proche?{v1.est_proche()}")
print("")
v1.arreter()
print(f"Est arrete maintenant?{v1.est_arrete()}")
help(AutoPilot)