import json
import Clients
import Plats


class Commandes:
    commandeslist = []
    latest_id = 0

    def __init__(self):
        self.load_data()
        Commandes.latest_id += 1
        self.commandeId = Commandes.latest_id
        self.idClient = Clients
        self.idPlats = Plats
        self.save_data()

    def CreerCommande(self):
        print("Créer une commande")
        instance_clients = Clients.Clients()
        instance_plats = Plats.Plats()
        print(instance_clients.displayAll())
        self.idClient = input("Entrez l'id du client : ")
        # Vérifiez si l'ID client saisi existe

        print(instance_plats.displayAll())
        self.idPlats = input("Entrez l'id du plat : ")
        # Vérifiez si l'ID plat saisi existe

        print(self.display())
        self.commandeslist.append(self.to_dict())
        self.save_data()

    def to_dict(self):
        return {
            "id": self.commandeId,
            "idClient": self.idClient,
            "NomClient": Clients.nom(self.idClient),
            "idPlats": self.idPlats
        }

    def load_data(self):
        try:
            with open('commandeslist.JSON', 'r') as file:
                Commandes.commandeslist = json.load(file)
                if Commandes.commandeslist:
                    Commandes.latest_id = Commandes.commandeslist[-1]['id']
                else:
                    Commandes.latest_id = 0
        except FileNotFoundError:
            Commandes.commandeslist = []
            Commandes.latest_id = 0

    def save_data(self):
        with open('commandeslist.JSON', 'w') as file:
            json.dump(Commandes.commandeslist, file, indent=2)

    def save_to_json(self, filename):
        with open(filename, "w") as json_file:
            json.dump(Commandes.commandeslist, json_file, indent=2)

    def display(self):
        return f"ID: {self.commandeId}, ID Client: {self.idClient}, ID Plat: {self.idPlats}"
