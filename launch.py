from fonctions_utile import  *
def launch():
    print(27 * '-+' + "\n{" + 20 * ' ' + "Bienvenue sur" + 19 * " " + "}" +
          "\n{" + 52 * ' ' + "}" + "\n{" + 21 * ' ' + "Code World" + 21 * " " +
          "}\n" + 27 * '+-' + "\n")
    print(19 * ' ' + "1/ \"New Game\"\n" + 19 * ' ' + "2/ \"Continue\"\n" +
          19 * ' ' + "3/ \"Credits\"\n")
    rep = str(input("entrez votre choix : "))
    while rep != "1" and rep != "2" and rep != "3":
        rep = str(input("entrez votre choix : "))
    if rep == "1":
        clearConsole()
        save_key = start("1")
    if rep == "2":
        clearConsole()
        save_key = start("2")
    if rep == "3":
        clearConsole()
        print("\n" + 28 * ' ' + "Crédits :\n" + "\n" + 13 * ' ' +
              "directeur projet/développeur/scénariste :\n" + 28 * ' ' +
              "Paul-Evan\n\n" + 15 * ' ' +
              "sous directeur projet/développeur :\n" + 28 * ' ' +
              "Théobald\n")
        save_key = ecran_accueil()
    return save_key