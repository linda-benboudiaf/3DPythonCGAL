# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from math import *

def initBoard():
    #Premier niveau un pion possible 
    b= box(pos=(  0, -4,  2), size= TailleCube) 
    b= box(pos=(  0, -4,  0), size= TailleCube)
    b= box(pos=( -2, -2,  2), size= TailleCube)
    b= box(pos=( -2, -2,  0), size= TailleCube)
    b= box(pos=(  0, -2,  2), size= TailleCube) # Pas de cube jumelle 
    #Deuxieme Niveau 
    b= box(pos=(  0, -6,  0), size= TailleCube)
    b= box(pos=(  0, -6, -2), size= TailleCube)
    b= box(pos=( -2, -4,  0), size= TailleCube)
    b= box(pos=( -2, -4, -2), size= TailleCube)
    b= box(pos=( -4, -2,  0), size= TailleCube)
    b= box(pos=( -4, -2, -2), size= TailleCube)
    #Vu arrière du plateau #Troisième niveau
    b= box(pos=(  0, -8, -2), size= TailleCube)
    b= box(pos=(  0, -8, -4), size= TailleCube)
    b= box(pos=( -2, -6, -2), size= TailleCube)
    b= box(pos=( -2, -6, -4), size= TailleCube)
    b= box(pos=( -4, -4, -2), size= TailleCube)
    b= box(pos=( -4, -4, -4), size= TailleCube)
    b= box(pos=( -6, -2, -2), size= TailleCube)
    b= box(pos=( -6, -2, -4), size= TailleCube)
    # Quatième Niveau vu arrière 
    b= box(pos=(  0,-10, -4), size= TailleCube)
    b= box(pos=(  0,-10, -6), size= TailleCube)
    b= box(pos=( -2, -8, -4), size= TailleCube)
    b= box(pos=( -2, -8, -6), size= TailleCube)
    b= box(pos=( -4, -6, -4), size= TailleCube)
    b= box(pos=( -4, -6, -6), size= TailleCube)
    b= box(pos=( -6, -4, -4), size= TailleCube)
    b= box(pos=( -6, -4, -6), size= TailleCube)
    b= box(pos=( -8, -2, -4), size= TailleCube)
    b= box(pos=( -8, -2, -6), size= TailleCube)
    # Dernier niveau
    b= box(pos=(  0,-12, -6), size= TailleCube)
    b= box(pos=( -2,-10, -6), size= TailleCube)
    b= box(pos=( -4, -8, -6), size= TailleCube)
    b= box(pos=( -6, -6, -6), size= TailleCube)
    b= box(pos=( -8, -4, -6), size= TailleCube)
    b= box(pos=(-10, -2, -6), size= TailleCube)

    # Pied du Plateau ...
    b= box(pos=(  0,-12, -8), size= TailleCube)
    b= box(pos=( -2,-12, -8), size= TailleCube)
    b= box(pos=( -4,-10, -8), size= TailleCube)
    b= box(pos=( -2,-10, -8), size= TailleCube)
    b= box(pos=( -6, -8, -8), size= TailleCube)
    b= box(pos=( -4, -8, -8), size= TailleCube)
    b= box(pos=( -8, -6, -8), size= TailleCube)
    b= box(pos=( -6, -6, -8), size= TailleCube)
    b= box(pos=(-10, -4, -8), size= TailleCube)
    b= box(pos=( -8, -4, -8), size= TailleCube)
    b= box(pos=(-10, -2, -8), size= TailleCube)

    board = []
    for i in range(48):
        board.append(b)
        label (pos=(0,0,0), text='This is a Cube')
    pass
    # Définition de la couleur du plateau (Des cubes quoi !!)
    for cube in scene.objects:
        if isinstance(cube, box):
            cube.color = vector(1,0.5, 1)
        pass
    pass

#def EventToCube (arg):
#        switcher={
#                b1 : return b1 
#        }
drag_pos = None

def take_obj(event):
        global drag_pos
#### BEGINNING GAMER ONE CUBES #####
        if event.pick == b1: 
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b1)
                scene.bind('mouseup', drop, b1) 
        elif event.pick == b2:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b2)
                scene.bind('mouseup', drop, b2)
                pass
        elif event.pick == b3:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b3)
                scene.bind('mouseup', drop, b3) 
                pass
        elif event.pick == b4: 
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b4)
                scene.bind('mouseup', drop, b4) 
        elif event.pick == b5:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b5)
                scene.bind('mouseup', drop, b5)
                pass
        elif event.pick == b6:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b6)
                scene.bind('mouseup', drop, b6) 
                pass
        elif event.pick == b7:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b7)
                scene.bind('mouseup', drop, b7)
                pass
        elif event.pick == b8:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b8)
                scene.bind('mouseup', drop, b8) 
                pass
        elif event.pick == b9: 
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b9)
                scene.bind('mouseup', drop, b9) 
        elif event.pick == b10:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b10)
                scene.bind('mouseup', drop, b10)
                pass
        elif event.pick == b11:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b11)
                scene.bind('mouseup', drop, b11) 
                pass
        elif event.pick == b12:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b12)
                scene.bind('mouseup', drop, b12) 
                pass
        elif event.pick == b13:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b13)
                scene.bind('mouseup', drop, b13)
                pass
        elif event.pick == b14:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b14)
                scene.bind('mouseup', drop, b14) 
                pass
        elif event.pick == b15: 
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b15)
                scene.bind('mouseup', drop, b15) 
        elif event.pick == b16:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b16)
                scene.bind('mouseup', drop, b16)
                pass
        elif event.pick == b17:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b17)
                scene.bind('mouseup', drop, b17)
                pass
        elif event.pick == b18:
                drag_pos = event.pickpos
                scene.bind('mousemove', move, b18)
                scene.bind('mouseup', drop, b18) 
                pass
##### END OF GAMER ONE CUBES #######


def move(evt, obj):
    global drag_pos # The initial mouse position. 
    new_pos = scene.mouse.project(normal=(0,0,1))
    if new_pos != drag_pos: # if mouse has moved.  
        obj.pos += new_pos - drag_pos 
        drag_pos = new_pos 
    pass

def drop(evt):
    scene.unbind('mousemove', move)
    scene.unbind('mouseup', drop)

def main():
    # Mettre en place Camèra + Lumière ...
    # Scene represente le monde "World" on definit certain paramètre initial... 
    global scene
    scene = display(x=0, y=0, title = 'Plateau.Inside', background=(0, 0, 0), width = 1000, height= 10000)
    scene.range = 5
    scene.autocenter = True
    # Lumière 
    local_light(pos=(10,10,0), color=color.white)
    global TailleCube
    TailleCube = vector(2,2,2)
    scene.bind('mousedown', take_obj)    
    initBoard() 
    initCube()
    jeu()

def initCube():       
    # Drag and Drop du Cube
    global cube



## Créer des cubes pour les joueur 18 pour chaqu'un + attribution de couleurs ...
def initCubesGamer1 (initColor, oppositeColor):
        label(pos=(14, -2, 4), text= "Gamer 1")
        global  b1, b2, b3,b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18
        b1= box(pos=(  12,  -2,  4), size= TailleCube, color = initColor) 
        b2= box(pos=(  15, -2, 4), size= TailleCube, color = initColor)
        b3= box(pos=(  18, -2, 4), size= TailleCube, color = initColor)
        b4= box(pos=(  21, -2,  4), size= TailleCube, color = initColor)
        b5= box(pos=(  12, -6,  4), size= TailleCube, color = initColor)
        b6= box(pos=(  15, -6,  4), size= TailleCube, color = initColor) 
        b7= box(pos=(  18, -6,  4), size= TailleCube, color = initColor)
        b8= box(pos=(  21, -6,  4), size= TailleCube, color = initColor)
        b9= box(pos=(  24, -10,  4), size= TailleCube, color = initColor)
        b10= box(pos=( 12, -10,  4), size= TailleCube, color = initColor)
        b11= box(pos=( 15, -10,  4), size= TailleCube, color = initColor)
        b12= box(pos=( 18, -10,  4), size= TailleCube, color = initColor)
        b13= box(pos=( 21, -10,  4), size= TailleCube, color = initColor)
        #Opposite Color       
        b14= box(pos=( 12, 0,  4), size= TailleCube, color = oppositeColor)
        b15= box(pos=( 15, 0,  4), size= TailleCube, color = oppositeColor)
        b16= box(pos=( 18, 0,  4), size= TailleCube, color = oppositeColor)
        b17= box(pos=( 21, 0,  4), size= TailleCube, color = oppositeColor)
        b18= box(pos=( 24, 0,  4), size= TailleCube, color = oppositeColor)

def initCubesGamer2 (initColor, oppositeColor):
        label(pos=(-14, -2, -4), text= "Gamer 2")
        global b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36
        b19= box(pos=( -12, -2,  -4), size= TailleCube, color = initColor) 
        b20= box(pos=( -15, -2,  -4) , size= TailleCube, color = initColor)
        b21= box(pos=( -18, -2,  -4) , size= TailleCube, color = initColor)
        b22= box(pos=( -21, -2,  -4), size= TailleCube, color = initColor)
        b23= box(pos=( -12, -6,  -4), size= TailleCube, color = initColor)
        b24= box(pos=( -15, -6,  -4), size= TailleCube, color = initColor) 
        b25= box(pos=( -18, -6,  -4), size= TailleCube, color = initColor)
        b26= box(pos=( -21, -6,  -4), size= TailleCube, color = initColor)
        b27= box(pos=( -24, -10, -4), size= TailleCube, color = initColor)
        b28= box(pos=( -12, -10, -4), size= TailleCube, color = initColor)
        b29= box(pos=( -15, -10, -4), size= TailleCube, color = initColor)
        b30= box(pos=( -18, -10, -4), size= TailleCube, color = initColor)
        b31= box(pos=( -21, -10, -4), size= TailleCube, color = initColor)
        #Opposite Color        
        b32= box(pos=( -12, 0,  -4), size= TailleCube, color = oppositeColor)
        b33= box(pos=( -15, 0,  -4), size= TailleCube, color = oppositeColor)
        b34= box(pos=( -18, 0,  -4), size= TailleCube, color = oppositeColor)
        b35= box(pos=( -21, 0,  -4), size= TailleCube, color = oppositeColor)
        b36= box(pos=( -24, 0,  -4), size= TailleCube, color = oppositeColor)

def jeu():
        jCouleur_yellow = vector(1,1,0)
        jCouleur_red = vector(1,0,0)
        jCouleur_ini = input("Choisissez la couleur Red (1, 0,0) or Yellow (1,1,0) \t")
        if jCouleur_ini == (1,1,0):
                initCubesGamer1(jCouleur_yellow, jCouleur_red )
                initCubesGamer2(jCouleur_red, jCouleur_yellow)
        elif jCouleur_ini == (1,0,0):
                initCubesGamer1(jCouleur_red, jCouleur_yellow)
                initCubesGamer2(jCouleur_yellow, jCouleur_red)
                pass
main()
