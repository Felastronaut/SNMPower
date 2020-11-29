#Le script va lire les données renvoyées dans un fichier txt par le script bash SNMP, puis
#puis va les convertir dans un format json, et les copier dans un fjchier JSON

import json

#On ouvre le fichier json de log, puis on recupere le dernier numero unique
with open('log.json', "r") as f1:
    last_line = f1.readlines()[-5]
    nombre_unique_str = last_line[3]
    nombre_unique_int = int(nombre_unique_str)

#On ouvre le contenu du fichier Raw de snmpget, puis on recepuere les informations qui nous interesse
with open('all.txt') as f:
    fln = f.readline()
    #On itere sur toutes les lignes
    while fln:
        ip_vari = str.strip(list(filter(None, fln.split(' ')))[-1])
        etat_vari = str.strip(list(filter(None, fln.split(' ')))[1])

        #On met ce que l'on veut écrire dans une variiable
        a_dict = {nombre_unique_int:{'IP': ip_vari, 'etat' : etat_vari}}

        #On ouvre et charge le fichier json pour les logs
        with open('log.json') as f2:
            data = json.load(f2)

        data.update(a_dict)

        #On ajoute le nouvel element dans le Json
        with open('log.json', 'w') as f2:
            json.dump(data, f2, indent =2)
        nombre_unique_int = nombre_unique_int+1
        #On passe a la ligne suivante
        fln = f.readline()
