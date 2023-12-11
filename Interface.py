import Clients
import Plats
import Commandes


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


def menuCommande():
    print("1. Créer une commande")
    print("2. Modifier une commande")
    print("3. Supprimer une commande")
    print("4. Afficher une commande")
    print("5. Afficher toutes les commandeslist")
    print("6. Quitter")
    choix = int(input("Choix: "))
    return choix

def interfaceCommande():
    choix = 0
    while choix != 6:
        choix = menuCommande()
        if choix == 1:
            commande = Commandes.Commandes()
            commande.CreerCommande()
            commande.save_to_json("commandeslist.json")
            print(commande.display())
        elif choix == 2:
            commande = Commandes.Commandes()
            commande.modifierCommande()
        elif choix == 3:
            commande = Commandes.Commandes()
            commande.supprimerCommande()
        elif choix == 4:
            commande = Commandes.Commandes()
            commande.displayUneCommande()
        elif choix == 5:
            commande = Commandes.Commandes()
            print(commande.displayAll())
        elif choix == 6:
            print("Au revoir")
        else:
            print("Choix invalide")