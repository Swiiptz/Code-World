import csv

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


#exporter sert à actualiser les csv-----------------------
def exporter(nom_fichier: str, dic: dict) -> None:
    """
  entrée: 
    nom_fichier    str    lieu d'écriture
    dic            dict   valeur à écrire
  pas de sortie, remplace ce qu'il y a dans le fichier par le dictionnaire entré
    """
    nom_colonnes = ['personnage', 'classe', 'progression', 'inventaire', 'emplacement']  #il faut mettre tous les headers dans cette liste
    fichier = open(nom_fichier + ".csv", 'w')
    with fichier:
        obj = csv.DictWriter(fichier, fieldnames=nom_colonnes, delimiter=" ")
        obj.writeheader()
        for i in dic:
            obj.writerow(dic[i])




