import json
import Categorie
class Plat:
    def __init__(self, nom, prix, description):
        self.nom = nom
        self.prix = prix
        self.description = description


    def display(self):
        return f"Nom: {self.nom}, Prix: {self.prix}, Description: {self.description}"

    def CreerPlat(self):
        self.nom = input("Entrez le nom du plat: ")
        self.prix = input("Entrez le prix du plat: ")
        self.description = input("Entrez la description du plat: ")

    def modifierPlat(self):
        self.nom = input("Entrez le nouveau nom du plat: ")
        self.prix = input("Entrez le nouveau prix du plat: ")
        self.description = input("Entrez la nouvelle description du plat: ")

    def supprimerPlat(self):
        self.nom = ""
        self.prix = ""
        self.description = ""

    def displayUnPlat(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}, Description: {self.description}")

    def displayAll(self):
        return f"Nom: {self.nom}, Prix: {self.prix}, Description: {self.description}"

    def save_to_json(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.__dict__, f, indent=4)

    def load_from_json(self, file_name):
        with open(file_name, "r") as f:
            self.__dict__ = json.load(f)