import csv
import sys
import json

##Classe qui verifie que l'IP est dans un format correct
class Solution(object):
   def validIPAddress(self, IP):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return True

ob = Solution()

def main():
   menu()


#Menu avec choix multiples
def menu():
    print("************Bienvenu dans le module de configuration**************")
    print()

    choice = input("""
                      A: Ajouter
                      B: Modifier
                      C: Supprimer
                      D: afficher
                      Q: Quitter

                      Choissisez une lettre: """)

    if choice == "A" or choice =="a":
        ajouter()
    elif choice == "B" or choice =="b":
        modifier()
    elif choice == "C" or choice =="c":
        supprimer()
    elif choice == "D" or choice =="d":
        afficher()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("Veuillez choisir entre A, B, C, D ou Q ")
        print("Votre choix")
        menu()


##############MODULE AJOUTER#########################3
#Permet d'ajouter un élément
def ajouter():
#On ouvre le fichier, puis on recupere le dernier identifiant de la lste
   with open('config.json', "r") as f1:
        last_line = f1.readlines()[-9]
        nombre_unique_str = last_line[3]
        nombre_unique_int = int(nombre_unique_str)
        nombre_unique_int = nombre_unique_int+1
   ## Ici on rentre les parametres d'un nouvel element
   nouvel_ip = input("Entrer un numero IP")
   #On verifie que l'IP est correcte, sinon on boucle
   while ob.validIPAddress(nouvel_ip) != True:
       nouvel_ip = input("Entrer un adresse IP correcte (xxx.xxx.xxx.xxx) : ")
   nouvel_commu = input("Entre un nom de communauté")
   nouvel_loca = input("Entrer une localisation")
   nouvel_descr = input("Entrer une description")
   nouvel_OID = input("Entrer un OID")
   nouvel_nom = input("Entrer un nom")

   #On rentre les parametres précedent dans une variable
   a_dict = {nombre_unique_int:{'IP': nouvel_ip, 'communaute' : nouvel_commu, 'localisation' : nouvel_loca, 'descrOID' : nouvel_descr, 'OID' : nouvel_OID, 'NAME' : nouvel_nom}}

   #On ouvre et charge le fichier json
   with open('config.json') as f:
       data = json.load(f)

   #On met à jour
   data.update(a_dict)

   #On ajoute le nouvel element dans le Json
   with open('config.json', 'w') as f:
       json.dump(data, f, indent =2)





##############MODULE AFFICHAGE########################
#Permet d'afficher un éléement précis dans la console
def afficher():
    #On ouvre le fichier json correspondant et on le charge
    with open("config.json", "r") as jsonFile:
        data_affich = json.load(jsonFile)
    choix_affich = input(""" Veuillez selectionner l'identifiant de l'élément à afficher

                      Choissisez un numero: """)

    try:
        print (data_affich[choix_affich])
    except Exception as e:
        print("""Erreur : Le numero n'est pas dans la base de données


        """, excep_key)

####################MODULE MODIFIER#############################
def modifier():
    with open("config.json", "r") as jsonFile:
        data_modif = json.load(jsonFile)
    choix_modif = input(""" Veuillez selectionner l'identifiant de l'élément à Modifier

                      Choissisez un numero: """)
    try:
        print (data_modif[choix_modif])
    except KeyError as excep_key :
        print("""Erreur : Le numero n'est pas dans la base de données


        """, excep_key)
    else :
        pass
    print (data_modif[choix_modif])
    confirm_modif = input ("""Souhaitez vous modifier cet élement? (celui-ci sera supprimé, puis il vous sera proposer de le re-ajouter)

                    1 : Oui
                    2 : Non
    """)
    if confirm_modif == "1":
        print("Vous rentrer dans la méthode supprimer")
        supprimer()
        print("Le numero que vous avez choisi à été supprimé, maintenant re-ajouter le avec les modifications")
        ajouter()
        print("Le numero à bien été modifié")
    elif confirm_modif == "2":
        print ("Annulation de la modification")
    else :
        print("Le numero n'existe pas")





########################MODULE SUPPRIMER################
#Permet de supprimer un élement précis
def supprimer():
   #On ouvre le fichier de condig
   a_file = open("config.json", "r")
   data_suppr = json.load(a_file)
   a_file.close()
   donnee_supp = input("Entrer le numero qu'il faut supprimer :")
   print (data_suppr[donnee_supp])
   choix_suppr = input("""On supprime?

            1 : Oui
            2: Non

        """)
   if choix_suppr == "1":
       try:
           del data_suppr[donnee_supp]
       except KeyError:
           print ("Le numéro choisi n'existe pas")
   elif choix_suppr == "2":
       print("Annulation de la suppression")
   else :
       print("Mauvais choix Veuillez recommencer")
   #On applique la suppression sur le fichier JSON
   a_file = open("config.json", "w")
   json.dump(data_suppr, a_file, indent=2)
   a_file.close()

main()