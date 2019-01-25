from Game import *

def main():
    print(sys.version)
    global choix 
    choix = input ("\n \n****** Welcome to INSIDE Social Game ****** \n Please choose play mode : \n Press 1 for Player vs Player \n Press 2 for Player vs Computer \n Press 3 for Computer vs Computer\n")
    if choix == 1:
        j1 = Joueur.Joueur(1, "Gamer 1")
        j2 = Joueur.Joueur(2, "Gamer 2")
        jeu = Jeu.Jeu(j1, j2)
        Plateau0.main(jeu)
        j1.set_cubes(Plateau0.boardJ1)
        j2.set_cubes(Plateau0.boardJ2)
        jeu.jouer()
        pass
    elif choix == 2:
        j1 = Joueur.Joueur(1, "Gamer 1")
        j2 = IA.IA(2, "Gamer 2")
        jeu = Jeu.Jeu(j1, j2)
        Plateau0.main(jeu)
        j1.set_cubes(Plateau0.boardJ1)
        j2.set_cubes(Plateau0.boardJ2)
        jeu.jouer()
        pass
    elif choix == 3: 
        j1 = IA.IA(1, "Gamer 1")
        j2 = IA.IA(2, "Gamer 2")
        jeu = Jeu.Jeu(j1, j2)
        Plateau0.main(jeu)
        j1.set_cubes(Plateau0.boardJ1)
        j2.set_cubes(Plateau0.boardJ2)
        jeu.jouer()
        pass
pass
main()
