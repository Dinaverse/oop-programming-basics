class Article:
    # Definition des attributs de la classe Article
    __reference: str
    __nom: str
    __prix_hors_taxes: float
    __quantite_en_stock: int

    # Constructeur
    def __init__(self, reference, nom, prix_hors_taxes, quantite_en_stock):
        self.__reference = reference
        self.__nom = nom
        self.__prix_hors_taxes = float(prix_hors_taxes)
        self.__quantite_en_stock = quantite_en_stock

    def afficher_info_article(self):
        print(f"Reference : {self.__reference}\nNom : {self.__nom}\nPrix HT : {self.__prix_hors_taxes:.2f}$\nEn stock : {self.__quantite_en_stock}")

    def get_nom(self):
        return self.__nom

    def get_prix_hors_taxes(self):
        return self.__prix_hors_taxes

    def get_quantite_en_stock(self):
        return self.__quantite_en_stock

    def set_prix_hors_taxes(self, prix_hors_taxes):
        if prix_hors_taxes < 0:
            print("❌ Prix invalide")
        else:
            self.__prix_hors_taxes = prix_hors_taxes

    def set_quantite_en_stock(self, quantite_en_stock):
        if quantite_en_stock < 0:
            print("❌ Quantite invalide")
        else:
            self.__quantite_en_stock = quantite_en_stock

    def approvisionner(self, nb_articles: int):
        self.__quantite_en_stock += nb_articles
        print(f"✅ {nb_articles} article(s) ajouté(s). Stock: {self.__quantite_en_stock}")

    def vendre(self, nb_articles: int):
        if nb_articles > self.__quantite_en_stock:
            print("❌ Vente non réussie : stock insuffisant.")
        else:
            self.__quantite_en_stock -= nb_articles
            prix_ttc = self.calculer_prix_total(nb_articles)
            print(f"✅ Vente réussie\nQuantité restante : {self.__quantite_en_stock}\nMontant total TTC : {prix_ttc:.2f}$")

    def calculer_prix_total(self, nb_articles: int):
        # Calcul avec TVA/GST (5% au Canada)
        prix_ht = self.__prix_hors_taxes * nb_articles
        prix_ttc = prix_ht * 1.15
        return prix_ttc


# -----------------Programme principale------------------
art1 = Article(125, "Lait", 5.85, 55)

art1.approvisionner(100)
art1.vendre(1000)
art1.vendre(15)
art1.afficher_info_article()