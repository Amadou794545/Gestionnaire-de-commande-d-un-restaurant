import json


class Clients:
    clients_list = []

    latest_id = 0

    def __init__(self, nom="", prenom="", phone=""):
        self.load_data()  # Charge les données existantes depuis le fichier JSON
        Clients.latest_id += 1
        self.id = Clients.latest_id
        self.nom = nom
        self.prenom = prenom
        self.phone = phone
        self.save_data()  # Sauvegarde les données dans le fichier JSON

    def load_data(self):
        try:
            with open('clients.JSON', 'r') as file:
                Clients.clients_list = json.load(file)
                if Clients.clients_list:
                    Clients.latest_id = Clients.clients_list[-1]['id']
                else:
                    Clients.latest_id = 0
        except FileNotFoundError:
            Clients.clients_list = []
            Clients.latest_id = 0

    def save_data(self):
        with open('clients.JSON', 'w') as file:
            json.dump(Clients.clients_list, file, indent=2)

    def CreerClient(self):
        print("Créer un client")
        self.nom = input("Nom: ")
        self.prenom = input("Prenom: ")
        self.phone = input("Phone: ")

        Clients.clients_list.append(self.to_dict())
        self.save_data()  # Sauvegarde les données dans le fichier JSON

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "phone": self.phone
        }

    def modifierClient(self):
        print("Modifier un client")
        print(self.displayAll())
        print("Qui voulez-vous modifier?")
        self.displayAll()
        choix = int(input("Choix: "))

        client_a_modifier = None
        for client in self.clients_list:
            if client['id'] == choix:
                client_a_modifier = client
                break

        if client_a_modifier:
            client_a_modifier['nom'] = input("Nom: ")
            client_a_modifier['prenom'] = input("Prenom: ")
            client_a_modifier['phone'] = input("Phone: ")
            print("Client modifié avec succès!")
        else:
            print("Choix invalide")

        self.save_data()

    def supprimerClient(self):
        print("Supprimer un client")
        print("Qui voulez-vous supprimer?")
        print(self.displayAll())
        choix = int(input("Choix: "))

        client_a_supprimer = None
        for client in self.clients_list:
            if client['id'] == choix:
                client_a_supprimer = client
                break

        if client_a_supprimer:
            self.clients_list.remove(client_a_supprimer)
            print("Client supprimé avec succès!")
        else:
            print("Choix invalide")

        self.save_data()

    def displayUnClient(self):
        print("Afficher un client")
        print("Qui voulez-vous afficher?")
        print(self.displayAll())
        choix = int(input("Choix: "))

        client_a_afficher = None
        for client in self.clients_list:
            if client['id'] == choix:
                client_a_afficher = client
                break

        if client_a_afficher:
            print(
                f"Client: {client_a_afficher['nom']} Prenom:{client_a_afficher['prenom']} Phone: {client_a_afficher['phone']} ID: {client_a_afficher['id']}")
        else:
            print("Choix invalide")

    def save_to_json(self, filename):
        with open(filename, "w") as json_file:
            json.dump(Clients.clients_list, json_file, indent=2)

    def load_from_json(self, filename):
        try:
            with open(filename, "r") as json_file:
                Clients.clients_list = json.load(json_file)
        except FileNotFoundError:
            print("File not found. No data loaded.")

    def display(self):
        return f"Client: {self.nom} Prenom:{self.prenom} Phone: {self.phone} ID: {self.id}"

    def displayAll(self):
        with open('clients.JSON') as mon_fichier:
            data = json.load(mon_fichier)
        return data
