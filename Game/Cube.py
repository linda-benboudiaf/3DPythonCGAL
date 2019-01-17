#!/usr/bin/python3.5
# -*-coding:Utf-8 -*
import random
class Cube:
    # Cube est reconnue par sa couleur.
    # Constructeur couleur initial
    def __init__(self, couleur, id ):
       self.couleur = couleur
       self.id = id
    def get_couleur(self):
        print("Couleur du Cube")
        return self.couleur
    def set_couleur (self, newCouleur):
        self.couleur = newCouleur
#Methode Main afin d'exec la class
if __name__ == '__main__':
    cube1 = Cube("Yellow", 1)
    cube2 = Cube("Marron", 2)
    print(cube2.id, cube1.id)
    #print(cube1.couleur, cube2.couleur)
    #cube2.set_couleur('Red')
    #print(cube2.couleur)
    board = []
    board.append(cube1.id)
    board.append(cube2.id)
    for i in (board):
        print(board)