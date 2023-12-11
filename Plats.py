import json
from enum import Enum

import Categorie
from Categorie import Categorie


class Plats:
    plats_list = []
    latest_id = 0

    def __init__(self, categories: Categorie = "", nom="", prix="", description=""):
        self.load_data()
        Plats.latest_id += 1
        self.id = self.latest_id
        self.nom = nom
        self.prix = prix
        self.categories = categories
        self.description = description
        self.save_data()

    def load_data(self):
        try:
            with open('plats.json', 'r') as file:
                content = file.read()
                if content:
                    Plats.plats_list = json.loads(content)
                    if Plats.plats_list:
                        Plats.latest_id = Plats.plats_list[-1]['id']
                    else:
                        Plats.latest_id = 0
                else:
                    Plats.plats_list = []
                    Plats.latest_id = 0
        except FileNotFoundError:
            Plats.plats_list = []
            Plats.latest_id = 0
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON : {e}")
            Plats.plats_list = []
            Plats.latest_id = 0

    def save_data(self):
        with open('plats.json', 'w') as file:
            json.dump(Plats.plats_list, file, indent=2, default=self.serialize_enum)

    def serialize_enum(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def display(self):
        return f"Nom: {self.nom}, Prix: {self.prix}, Description: {self.description},Categorie: {self.categories}, ID: {self.id}"

    def CreerPlat(self):
        print("Créer un plat")
        self.nom = input("Entrez le nom du plat: ")
        self.prix = input("Entrez le prix du plat: ")
        self.description = input("Entrez la description du plat: ")
        print("Entrez la catégorie du plat: ")
        print("1. Entrée")
        print("2. Plat")
        print("3. Dessert")
        choix = int(input("Choix: "))
        if choix == 1:
            self.categories = Categorie.ENTREE
        elif choix == 2:
            self.categories = Categorie.PLAT
        elif choix == 3:
            self.categories = Categorie.DESSERT
        else:
            print("Choix invalide")

        Plats.plats_list.append(self.to_dict())
        self.save_data()

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": self.prix,
            "description": self.description,
            "categories": self.categories
        }

    def modifierPlat(self):
        print("Modifier un plat")
        print(self.displayAll())
        print("Lequel voulez-vous modifier?")
        choix = int(input("Choix: "))
        plat_a_modifier = None
        for plat in self.plats_list:
            if plat['id'] == choix:
                plat_a_modifier = plat
                break
        if plat_a_modifier:
            plat_a_modifier['nom'] = input("Nom: ")
            plat_a_modifier['prix'] = input("Prix: ")
            plat_a_modifier['description'] = input("Description: ")
            print("Plat modifié avec succès!")
        else:
            print("Choix invalide")
        self.save_data()

    def supprimerPlat(self):
        print("Supprimer un plat")
        print(self.displayAll())
        print("Lequel voulez-vous supprimer?")
        choix = int(input("Choix: "))
        plat_a_supprimer = None
        for plat in self.plats_list:
            if plat['id'] == choix:
                plat_a_supprimer = plat
                break
        if plat_a_supprimer:
            self.plats_list.remove(plat_a_supprimer)
            print("Plat supprimé avec succès!")
        else:
            print("Choix invalide")
        self.save_data()

    def displayUnPlat(self):
        print("Afficher un plat")
        print(self.displayAll())
        print("Lequel voulez-vous afficher?")
        choix = int(input("Choix: "))
        plat_a_afficher = None
        for plat in self.plats_list:
            if plat['id'] == choix:
                plat_a_afficher = plat
                break
        if plat_a_afficher:
            print(
                f"Nom: {plat_a_afficher['nom']}, Prix: {plat_a_afficher['prix']}, Description: {plat_a_afficher['description']}, Categorie: {plat_a_afficher['categories']}")
        else:
            print("Choix invalide")

    def displayAll(self):
        with open('plats.json') as mon_fichier:
            data = json.load(mon_fichier)
        return data
    def save_to_json(self, filename):
        with open(filename, "w") as json_file:
            json.dump(Plats.plats_list, json_file, indent=2,default=self.serialize_enum)

    def load_from_json(self):
        try:
            with open("plats.json", "r") as json_file:
                Plats.plats_list = json.load(json_file)
        except FileNotFoundError:
            print("File not found. No data loaded.")

    def platExists(self, plat_id):
        # Vérifiez si l'ID plat existe dans la liste des plats
        for plat in self.plats_list:
            if plat['id'] == plat_id:
                return True
        return False
