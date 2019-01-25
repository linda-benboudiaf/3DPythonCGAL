from Game import *

def main():
    print(sys.version)
    #py = Pyramide.Pyramide()
    j1 = Joueur.Joueur(1, "j1")
    j2 = Joueur.Joueur(2, "j2")
    jeu = Jeu.Jeu(j1, j2)
    Plateau0.main(jeu)
    Plateau0.test()
    #jeu.jouer()
    #po = py.plateau[4].etageArray[0]
    #py.pose(4, po)
pass

main()
