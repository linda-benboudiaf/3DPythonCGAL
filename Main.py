from Game import *

def main():
    print(sys.version)
    j1 = IA.IA(1, "j1")
    j2 = IA.IA(2, "j2")
    jeu = Jeu.Jeu(j1, j2)
    Plateau0.main(jeu)
    j1.set_cubes(Plateau0.boardJ1)
    j2.set_cubes(Plateau0.boardJ2)
    jeu.jouer()
pass

main()
