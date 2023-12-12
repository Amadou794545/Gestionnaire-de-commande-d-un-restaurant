import Clients
import Interface


def main():
    print("Bienvenue au restaurant")
    print("Que voulez-vous faire?")
    print("1. Client")
    print("2. Plat")
    print("3. Commande")
    choix = int(input("Choix: "))
    if choix == 1:
        Interface.interfaceClient()
    elif choix == 2:
        Interface.interfacePlat()
    elif choix == 3:
        Interface.interfaceCommande()
    else:
        print("Choix invalide")



main()
