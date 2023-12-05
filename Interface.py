import Clients



def menu():
    print("1. Créer un client")
    print("2. Modifier un client")
    print("3. Supprimer un client")
    print("4. Afficher un client")
    print("5. Afficher tous les clients")
    print("6. Quitter")
    choix = int(input("Choix: "))
    return choix

def interface():
        choix = 0
        while choix != 6:
            choix = menu()
            if choix == 1:
                client = Clients.Clients()
                client.CreerClient()
                client.save_to_json("clients.JSON")
                print(client.display())
            elif choix == 2:
                client = Clients.Clients()
                client.modifierClient()
                print(client.display())
            elif choix == 3:
                client = Clients.Clients()
                client.supprimerClient()
                print(client.display())
            elif choix == 4:
                client = Clients.Clients()
                client.displayUnClient()
                print(client.display())
            elif choix == 5:
                client = Clients.Clients()
                print(client.displayAll())
            elif choix == 6:
                print("Au revoir")
            else:
                print("Choix invalide")
