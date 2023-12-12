import json
from Clients import Clients
from Plats import Plats


class Commandes:
    commandeslist = []
    latest_id = 0

    def __init__(self):
        self.load_data()
        Commandes.latest_id += 1
        self.commandeId = Commandes.latest_id
        self.clients_instance = Clients()  # Create an instance of Clients
        self.idClient = None
        self.idPlats = []
        self.save_data()

    def CreerCommande(self):
        print("Créer une commande")
        instance_clients = Clients()
        instance_plats = Plats()

        print(instance_clients.displayAll())
        idclient = int(input("Entrez l'id du client : "))

        # Check if the entered client ID exists
        client_exists = False
        for client in instance_clients.clients_list:
            if client['id'] == idclient:
                client_exists = True
                break

        if not client_exists:
            print(f"Client with ID {idclient} does not exist.")
            return

        self.idClient = idclient

        # Allow the client to order multiple dishes
        self.idPlats = []
        while True:
            print(instance_plats.displayAll())
            idplat = int(input("Entrez l'id du plat (0 to finish): "))

            if idplat == 0:
                break  # Stop ordering when 0 is entered

            # Check if the entered plat ID exists
            plat_exists = False
            for plat in instance_plats.plats_list:
                if plat['id'] == idplat:
                    plat_exists = True
                    break

            if not plat_exists:
                print(f"Plat with ID {idplat} does not exist. Please enter a valid ID.")
                continue

            self.idPlats.append(idplat)

        # Create a dictionary representing the order
        temp = self.to_dict()
        self.commandeslist.append(temp)
        self.save_data()

    def to_dict(self):
        clients_data = self.clients_instance.load_from_json("clients.JSON")
        idclients = ""
        idclients1 = 0
        for client in clients_data:
            if client['id'] == self.idClient:
                idclients1 = client['id']
                idclients = client['nom']
                break  # Stop the loop once the client is found

        plats_data = Plats.load_from_json("plats.json")
        if plats_data is None:
            raise ValueError("Plats data is None. Check the load_from_json method in the Plats module.")

        idplats = []
        idplats1 = []
        idplats2 = []
        for plat_id in self.idPlats:
            for plat in plats_data:
                if plat['id'] == plat_id:
                    idplats.append(plat['id'])
                    idplats1.append(plat['nom'])
                    idplats2.append(plat['prix'])
                    break

        # Convert idplats2 elements to integers
        idplats2 = [int(price) for price in idplats2]

        # Check if the client or plat was not found
        if idclients1 == 0:
            raise ValueError(f"Client with id {self.idClient} not found in clients_data")

        return {
            "id": self.commandeId,
            "idClient": idclients1,
            "NomClient": idclients,
            "idPlats": idplats,
            "NomPlats": idplats1,
            "PrixPlats": idplats2,
            "Total": sum(idplats2)
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
        return f"ID: {self.commandeId}, ID Client: {self.idClient}, ID Plats: {self.idPlats}"

    def displayAll(self):
        with open('commandeslist.JSON') as mon_fichier:
            data = json.load(mon_fichier)
        return data

    @staticmethod
    def load_from_json(filename):
        try:
            with open(filename, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print("File not found. No data loaded.")

    def displayFacture(self):
        print("Afficher l'historique des commandes d'un client")
        clients_data = self.clients_instance.displayAll()

        # Display client details
        print("Liste des clients:")
        for client in clients_data:
            print(f"ID: {client['id']}, Nom: {client['nom']}")

        print("Lequel voulez-vous afficher?")
        choix = int(input("Choix: "))

        commande_data = self.load_from_json("commandeslist.JSON")

        # Display command details for the chosen client
        found_commandes = []
        for commande in commande_data:
            if commande['idClient'] == choix:
                found_commandes.append(commande)

        if not found_commandes:
            print(f"Aucune commande trouvée pour le client avec l'ID {choix}.")
            return

        print(f"\nCommandes pour le client avec l'ID {choix}:")
        for commande_a_afficher in found_commandes:
            prix_plats = [float(prix) for prix in commande_a_afficher['PrixPlats']]
            total = sum(prix_plats)
            print(
                f"Name Plats: {commande_a_afficher['NomPlats']}, Prix: {commande_a_afficher['PrixPlats']}, Total: {total}")
