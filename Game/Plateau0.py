# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from math import *
import Point

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
        label (pos=(0,0,0), text='Inside Board')
    pass
    # Définition de la couleur du plateau (Des cubes quoi !!)
    for cube in scene.objects:
        if isinstance(cube, box):
            cube.color = vector(1, 0.4, 0.5)
        pass
    pass

def initSystemD():
    global boardD
    boardD = []
    global d400
    d400 = box(pos=(0, -2, 0), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d400)
    jeu.py.get_pion(0, Point.Point(0, 0)).refBox = d400

    global d401
    d401 = box(pos=(0, -4, -2), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d401)
    global d410
    d410 = box(pos=(0, -6, -4), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d410)
    global d411
    d411 = box(pos=(0, -8, -6), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d411)
    global d402
    d402 = box(pos=(0, -10, -8), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d402)
    global d420
    d420 = box(pos=(-2, -2, -2), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d420)
    global d412
    d412 = box(pos=(-2, -4, -4), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d412)
    global d421
    d421 = box(pos=(-2, -6, -6), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d421)
    global d422
    d422 = box(pos=(-2, -8, -8), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d422)
    global d403
    d403 = box(pos=(-4, -2, -4), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d403)
    global d430
    d430 = box(pos=(-4, -4, -6), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d430)
    global d413
    d413 = box(pos=(-4, -6, -8), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d413)
    global d431
    d431 = box(pos=(-6, -2, -6), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d431)
    global d404
    d404 = box(pos=(-6, -4, -8), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d404)
    global d440
    d440 = box(pos=(-8, -2, -8), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d440)
    global d300
    d300 = box(pos=(0, -2, -2), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d300)
    global d301
    d301 = box(pos=(0, -4, -4), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d301)
    global d310
    d310 = box(pos=(0, -6, -6), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d310)
    global d311
    d311 = box(pos=(0, -8, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d311)
    global d320
    d320 = box(pos=(-2, -2, -4), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d320)
    global d302
    d302 = box(pos=(-2, -4, -6), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d302)
    global d321
    d321 = box(pos=(-2, -6, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d321)
    global d303
    d303 = box(pos=(-4, -4, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d303)
    global d312
    d312 = box(pos=(-4, -2, -6), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d312)
    global d330
    d330 = box(pos=(-6, -2, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d330)
    global d200
    d200 = box(pos=(0, -2,-4 ), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d200)
    global d201
    d201 = box(pos=(0, -4, -6), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d201)
    global d210
    d210 = box(pos=(0, -6, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d210)
    global d211
    d211 = box(pos=(-2, -2,-6 ), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d211)
    global d220
    d220 = box(pos=(-2, -4, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d220)
    global d202
    d202 = box(pos=(-4, -2, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d202)
    global d100
    d100 = box(pos=(0, -2, -6 ), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d100)
    global d110
    d110 = box(pos=(0, -4, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d110)
    global d101
    d101 = box(pos=(-2, -2, -8), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d101)
    global d000
    d000 = box(pos=(0,-2 ,-8 ), size= TailleCube, color=color.white, opacity=0.2, visible=False)
    boardD.append(d000)

def focus(i):
    boardD[i].color = color.red

def unfocus(i):
    boardD[i].color = color.white

def test():
    newFocus = 0
    pastFocus = 0
    d400.color = color.green
    while True:
        if scene.kb.keys: # une touche a-t-elle ete appuyee ?
            touche = scene.kb.getkey() # de quelle touche s'agit-il ?
            if touche == 'up' or touche == 'down':
                # la touche fleche vers le haut ou vers le bas
                if touche == 'up':
                    if newFocus < 34 : # le rayon des balles augmente
                        pastFocus = newFocus
                        newFocus += 1
                else:
                    if newFocus > 0: # le rayon des balles augmente
                        pastFocus = newFocus
                        newFocus -= 1
            # fin traitement touches 'up' ou 'down'
        # fin traitement touches clavier
        unfocus(pastFocus)
        focus(newFocus)
        rate(100)

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
    ##### BEGINNING OF GAMER TWO CUBES #####
    if event.pick == b19:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b19)
            scene.bind('mouseup', drop, b19)
            pass
    elif event.pick == b20:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b20)
            scene.bind('mouseup', drop, b20)
            pass
    elif event.pick == b21:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b21)
            scene.bind('mouseup', drop, b21)
            pass
    elif event.pick == b22:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b22)
            scene.bind('mouseup', drop, b22)
            pass
    elif event.pick == b23:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b23)
            scene.bind('mouseup', drop, b23)
            pass
    elif event.pick == b24:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b24)
            scene.bind('mouseup', drop, b24)
            pass
    elif event.pick == b25:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b25)
            scene.bind('mouseup', drop, b25)
            pass
    elif event.pick == b26:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b26)
            scene.bind('mouseup', drop, b26)
            pass
    elif event.pick == b27:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b27)
            scene.bind('mouseup', drop, b27)
            pass
    elif event.pick == b28:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b28)
            scene.bind('mouseup', drop, b28)
            pass
    elif event.pick == b29:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b29)
            scene.bind('mouseup', drop, b29)
            pass
    elif event.pick == b30:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b30)
            scene.bind('mouseup', drop, b30)
            pass
    elif event.pick == b31:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b31)
            scene.bind('mouseup', drop, b31)
            pass
    elif event.pick == b32:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b32)
            scene.bind('mouseup', drop, b32)
            pass
    elif event.pick == b33:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b33)
            scene.bind('mouseup', drop, b33)
            pass
    elif event.pick == b34:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b34)
            scene.bind('mouseup', drop, b34)
            pass
    elif event.pick == b35:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b35)
            scene.bind('mouseup', drop, b35)
            pass
    elif event.pick == b36:
            drag_pos = event.pickpos
            scene.bind('mousemove', move, b36)
            scene.bind('mouseup', drop, b36)
            pass

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

def initCube():
    # Drag and Drop du Cube
    global cube

## Créer des cubes pour les joueur 18 pour chaqu'un + attribution de couleurs ...
def initCubesGamer1 (initColor, oppositeColor):
    label(pos=(14, -2, 4), text= "Gamer 1")
    global  b1, b2, b3,b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18
    b1= box(pos=(  12,  -2,  -10), size= TailleCube, color = initColor)
    b2= box(pos=(  15, -2, -10), size= TailleCube, color = initColor)
    b3= box(pos=(  18, -2, -10), size= TailleCube, color = initColor)
    b4= box(pos=(  21, -2,  -10), size= TailleCube, color = initColor)
    b5= box(pos=(  12, -6,  -10), size= TailleCube, color = initColor)
    b6= box(pos=(  15, -6,  -10), size= TailleCube, color = initColor)
    b7= box(pos=(  18, -6,  -10), size= TailleCube, color = initColor)
    b8= box(pos=(  21, -6,  -10), size= TailleCube, color = initColor)
    b9= box(pos=(  24, -10,  -10), size= TailleCube, color = initColor)
    b10= box(pos=( 12, -10,  -10), size= TailleCube, color = initColor)
    b11= box(pos=( 15, -10,  -10), size= TailleCube, color = initColor)
    b12= box(pos=( 18, -10,  -10), size= TailleCube, color = initColor)
    b13= box(pos=( 21, -10,  -10), size= TailleCube, color = initColor)
    #Opposite Color
    b14= box(pos=( 12, 0,  -10), size= TailleCube, color = oppositeColor)
    b15= box(pos=( 15, 0,  -10), size= TailleCube, color = oppositeColor)
    b16= box(pos=( 18, 0,  -10), size= TailleCube, color = oppositeColor)
    b17= box(pos=( 21, 0,  -10), size= TailleCube, color = oppositeColor)
    b18= box(pos=( 24, 0,  -10), size= TailleCube, color = oppositeColor)

def initCubesGamer2 (initColor, oppositeColor):
    label(pos=(-14, -2, -4), text= "Gamer 2")
    global b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36
    b19= box(pos=( -12, -2,  -10), size= TailleCube, color = initColor)
    b20= box(pos=( -15, -2,  -10) , size= TailleCube, color = initColor)
    b21= box(pos=( -18, -2,  -10) , size= TailleCube, color = initColor)
    b22= box(pos=( -21, -2,  -10), size= TailleCube, color = initColor)
    b23= box(pos=( -12, -6,  -10), size= TailleCube, color = initColor)
    b24= box(pos=( -15, -6,  -10), size= TailleCube, color = initColor)
    b25= box(pos=( -18, -6,  -10), size= TailleCube, color = initColor)
    b26= box(pos=( -21, -6,  -10), size= TailleCube, color = initColor)
    b27= box(pos=( -24, -10, -10), size= TailleCube, color = initColor)
    b28= box(pos=( -12, -10, -10), size= TailleCube, color = initColor)
    b29= box(pos=( -15, -10, -10), size= TailleCube, color = initColor)
    b30= box(pos=( -18, -10, -10), size= TailleCube, color = initColor)
    b31= box(pos=( -21, -10, -10), size= TailleCube, color = initColor)
    #Opposite Color
    b32= box(pos=( -12, 0,  -10), size= TailleCube, color = oppositeColor)
    b33= box(pos=( -15, 0,  -10), size= TailleCube, color = oppositeColor)
    b34= box(pos=( -18, 0,  -10), size= TailleCube, color = oppositeColor)
    b35= box(pos=( -21, 0,  -10), size= TailleCube, color = oppositeColor)
    b36= box(pos=( -24, 0,  -10), size= TailleCube, color = oppositeColor)

def jeu():
    jCouleur_yellow = vector(1,1,0)
    jCouleur_red = vector(1,0,0)
    initCubesGamer1(jCouleur_yellow, jCouleur_red )
    initCubesGamer2(jCouleur_red, jCouleur_yellow)
    #jCouleur_ini = input("Choisissez la couleur Red (1, 0,0) or Yellow (1,1,0) \t")
    #if jCouleur_ini == (1,1,0):
    #    initCubesGamer1(jCouleur_yellow, jCouleur_red )
    #    initCubesGamer2(jCouleur_red, jCouleur_yellow)
    #elif jCouleur_ini == (1,0,0):
    #    initCubesGamer1(jCouleur_red, jCouleur_yellow)
    #    initCubesGamer2(jCouleur_yellow, jCouleur_red)
    #pass

def main(jeuInput):
    global jeu
    jeu = jeuInput
    # Mettre en place Camèra + Lumière ...
    # Scene represente le monde "World" on definit certain paramètre initial...
    global scene
    global drag_pos
    drag_pos = None
    scene = display(x=0, y=0, title = 'Plateau.Inside', background=(0, 0, 0), width = 1000, height= 10000)
    scene.range = 5
    scene.autocenter = True
    # Lumière
    local_light(pos=(10,10,0), color=color.yellow)
    global TailleCube
    TailleCube = vector(2,2,2)
    scene.bind('mousedown', take_obj)
    initBoard()
    initCube()
    initSystemD()
    jeu()
