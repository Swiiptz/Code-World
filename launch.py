from fonctions_utile import *
from save import *


def launch():
  print(27 * '-+' + "\n{" + 20 * ' ' + "Bienvenue sur" + 19 * " " + "}" +
        "\n{" + 52 * ' ' + "}" + "\n{" + 21 * ' ' + "Code World" + 21 * " " +
        "}\n" + 27 * '+-' + "\n")
  print(19 * ' ' + "1/ New Game\n" + 19 * ' ' + "2/ Continue\n" + 19 * ' ' +
        "3/ Credits\n")
  rep = str(input("entrez votre choix : "))
  while rep != "1" and rep != "2" and rep != "3":
    rep = str(input("entrez votre choix : "))
  if rep == "1":
    save_key = start("1")
  if rep == "2":
    clearConsole()
    save_key = start("2")
  if rep == "3":
    clearConsole()
    print("\n" + 28 * ' ' + "Crédits :\n" + "\n" + 13 * ' ' +
          "directeur projet/développeur/scénariste :\n" + 28 * ' ' +
          "Paul-Evan\n\n" + 15 * ' ' +
          "sous directeur projet/développeur :\n" + 28 * ' ' + "Théobald\n")
    save_key = launch()
    dic_save[save_key] = {"personnage": save_key}
    exporter("save", dic_save)
  return save_key


def start(choix):
  clearConsole()
  if choix == '1':  #1/ New Game
    print("Bienvenue !\nDite moi..Comment vous appelez vous ?")
    save_key = input("choix pseudo : ")

    print(f"{save_key} c'est ça ?")
    verif = input("oui/non : ")
    if verif == 'oui':
      return save_key
    else:
      start(choix)
  elif choix == '2':  #2/ continuer
    print("Quel est votre nom déjà ?")
    with open("save.csv", newline='') as csvfile:
      doc = csv.reader(csvfile, delimiter=' ')
      tab = []
      for i in doc:
        tab.append(i)
    for i in range(len(tab) - 1):
      print(f"{i+1}/ {tab[i+1][0]}")
    print(tab)
    #choix = input("1/2/... : ")
    #1 verifier si le nom est dans le tab
    tab_pseudo = {}
    for i in range(len(tab) - 1):  # creation di de pseudo
      tab_pseudo = (tab[i + 1][0])
    print(tab_pseudo)
    #2 demander mdp associé
    #3 verifier mdp
