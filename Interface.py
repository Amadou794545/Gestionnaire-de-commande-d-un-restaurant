import Clients
import Plats


def menuClient():
    print("1. Créer un client")
    print("2. Modifier un client")
    print("3. Supprimer un client")
    print("4. Afficher un client")
    print("5. Afficher tous les clients")
    print("6. Quitter")
    choix = int(input("Choix: "))
    return choix


def interfaceClient():
    choix = 0
    while choix != 6:
        choix = menuClient()
        if choix == 1:
            client = Clients.Clients()
            client.CreerClient()
            client.save_to_json("clients.JSON")
            print(client.display())
        elif choix == 2:
            client = Clients.Clients()
            client.modifierClient()
        elif choix == 3:
            client = Clients.Clients()
            client.supprimerClient()
        elif choix == 4:
            client = Clients.Clients()
            client.displayUnClient()
        elif choix == 5:
            client = Clients.Clients()
            print(client.displayAll())
        elif choix == 6:
            print("Au revoir")
        else:
            print("Choix invalide")


def menuPlat():
    print("1. Créer un plat")
    print("2. Modifier un plat")
    print("3. Supprimer un plat")
    print("4. Afficher un plat")
    print("5. Afficher tous les plats")
    print("6. Quitter")
    choix = int(input("Choix: "))
    return choix


def interfacePlat():
    choix = 0
    while choix != 6:
        choix = menuPlat()
        if choix == 1:
            plat = Plats.Plats()
            plat.CreerPlat()
            plat.save_to_json("plats.json")
            print(plat.display())
        elif choix == 2:
            plat = Plats.Plats()
            plat.modifierPlat()
        elif choix == 3:
            plat = Plats.Plats()
            plat.supprimerPlat()
        elif choix == 4:
            plat = Plats.Plats()
            plat.displayUnPlat()
        elif choix == 5:
            plat = Plats.Plats()
            print(plat.displayAll())
        elif choix == 6:
            print("Au revoir")
        else:
            print("Choix invalide")
