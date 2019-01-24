import Cube
class Plateau:

    nb_cube = 36
    i = 0
    def __init__(self):
        #Definition des attribut du plateau de jeu
        self.taille = 15

if __name__ == '__main__':

    board = []
    c1 = Cube("Marron", 1)
    c2 = Cube("Marron", 2)
    c3 = Cube("Marron", 3)
    c4 = Cube("Marron", 4)
    c5 = Cube("Marron", 5)
    c6 = Cube("Marron", 6)
    c7 = Cube("Marron", 7)
    c8 = Cube("Marron", 8)
    c9 = Cube("Marron", 9)
    c10 = Cube("Marron", 10)
    c11 = Cube("Marron", 11)
    c12 = Cube("Marron", 12)
    c13 = Cube("Marron", 13)
    c14 = Cube("Marron", 14)
    c15 = Cube("Marron", 15)

    board.append(c1.id)
    board.append(c2.id)
    board.append(c3.id)
    board.append(c4.id)
    board.append(c5.id)
    board.append(c6.id)
    board.append(c7.id)
    board.append(c8.id)
    board.append(c9.id)
    board.append(c10.id)
    board.append(c11.id)
    board.append(c12.id)
    board.append(c13.id)
    board.append(c14.id)
    board.append(c15.id)
    for i in range(15):
        print(board)



