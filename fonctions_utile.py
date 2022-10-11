import os
import csv

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def lit_fichier(nom_fichier: str) -> dict:
    dic_rep = {}
    #on charge le fichier et on le transforme en liste
    nom_fichier += ".csv"
    with open(nom_fichier, mode='r') as fichier_ouvert:
        tab_rep = list(csv.DictReader(fichier_ouvert, delimiter=" "))
    dic_rep = {}

    if nom_fichier == "save.csv":
        clé = "personnage"
    else :
        clé = "id"

    for i in tab_rep:
        dic_rep[i[clé]] = i
    return dic_rep