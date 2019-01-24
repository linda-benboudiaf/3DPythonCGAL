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

def initSystemD():
    global boardD
    boardD = []
    global d400
    d400 = box(pos=(0, -2, 0), size= TailleCube, color=color.white, opacity=0.2, visible=True)
    boardD.append(d400)
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

def take_obj(event):
    global drag_pos
    if event.pick == cube:
        drag_pos = event.pickpos
        scene.bind('mousemove', move, cube)
        scene.bind('mouseup', drop, cube) #Drop the cube man !!
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
    cube = box(pos=(4, -2, -8), size=TailleCube,color= color.yellow)
    drag_pos = None

    scene.bind('mousedown', take_obj)


## Créer des cubes pour les joueur 18 pour chaqu'un + attribution de couleurs ...
def initCubesGamer1 (initColor, oppositeColor):
    label(pos=(14, -2, 4), text= "Gamer 1")
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

    initBoard()
    initCube()
    initSystemD()
    jeu()
