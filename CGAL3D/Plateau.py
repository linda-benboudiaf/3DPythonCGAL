# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from math import *

# Mettre en place Camèra + Lumière ...
# Scene represente le monde "World" on definit certain paramètre initial... 
scene = display(x=0, y=0, title = 'Plateau.Inside', background=(1, 1, 1))
scene.range = 5
scene.autocenter = True
# Lumière 
local_light(pos=(-10,-10,10), color=color.yellow)
TailleCube = vector(2,2,2)
#Premier niveau un pion possible 
b= box(pos=(0, -4,2), size= TailleCube) 
b= box(pos=(0,-4,0), size=TailleCube)
b= box (pos=(-2,-2,2), size=TailleCube)
b= box (pos=(-2,-2,0), size=TailleCube)
b= box(pos=(0,-2,2), size=TailleCube) # Pas de cube jumelle 
#Deuxieme Niveau 
b= box(pos=(0,-6,0), size=TailleCube)
b= box(pos=(0,-6,-2), size=TailleCube)
b= box(pos=(-2,-4,0), size=TailleCube)
b= box(pos=(-2,-4,-2), size=TailleCube)
b= box(pos=(-4,-2,0), size=TailleCube)
b= box(pos=(-4,-2,-2), size=TailleCube)
#Vu arrière du plateau #Troisième niveau
b= box(pos=(0,-8,-2), size=TailleCube)
b= box(pos=(0,-8,-4), size=TailleCube)
b= box(pos=(-2,-6,-2), size=TailleCube)
b= box(pos=(-2,-6,-4), size=TailleCube)
b= box(pos=(-4,-4,-2), size=TailleCube)
b= box(pos=(-4,-4,-4), size=TailleCube)
b= box(pos=(-6,-2,-2), size=TailleCube)
b= box(pos=(-6,-2,-4), size=TailleCube)
# Quatième Niveau vu arrière 
b= box(pos=(0,-10,-4),size=TailleCube)
b= box(pos=(0,-10,-6),size=TailleCube)
b= box(pos=(-2,-8,-4), size=TailleCube)
b= box(pos=(-2,-8,-6), size=TailleCube)
b= box(pos=(-4,-6,-4), size=TailleCube)
b= box(pos=(-4,-6,-6), size=TailleCube)
b= box(pos=(-6,-4,-4), size=TailleCube)
b= box(pos=(-6,-4,-6), size=TailleCube)
b= box(pos=(-8,-2,-4), size=TailleCube)
b= box(pos=(-8,-2,-6), size=TailleCube)
# Dernier niveau
b= box(pos=(0,-12,-6), size=TailleCube)
b= box(pos=(-2,-10,-6), size=TailleCube)
b= box(pos=(-4,-8,-6), size=TailleCube)
b= box(pos=(-6,-6,-6), size=TailleCube)
b= box(pos=(-8,-4,-6), size=TailleCube)
b= box(pos=(-10,-2,-6), size=TailleCube)

# Pied du Plateau ...
b= box(pos=(0,-12,-8), size=TailleCube)
b= box(pos=(-2,-12,-8), size=TailleCube)
b= box(pos=(-4,-10,-8), size=TailleCube)
b= box(pos=(-2,-10,-8), size=TailleCube)
b= box(pos=(-6,-8,-8), size=TailleCube)
b= box(pos=(-4,-8,-8), size=TailleCube)
b= box(pos=(-8,-6,-8), size=TailleCube)
b= box(pos=(-6,-6,-8), size=TailleCube)
b= box(pos=(-10,-4,-8), size=TailleCube)
b= box(pos=(-8,-4,-8), size=TailleCube)
b= box(pos=(-10,-2,-8), size=TailleCube)

board = []
for i in range(48):
        board.append(b)
        label (pos=(0,0,0), text='This is a Cube')
        


# Définition de la couleur du plateau (Des cubes quoi !!)
CouleurChoco = vector(86.7,39.26,17.69)
for cube in scene.objects:
    if isinstance(cube, box):
        cube.color = vector(1,0.5, 1)
        
# Drag and Drop du Cube
cube = box(pos=(0, -2, 8), size=TailleCube,color= color.yellow)
drag_pos = None
def take_obj(event):
    global drag_pos
    if event.pick == cube:
        drag_pos = event.pickpos
        scene.bind('mousemove', move, cube)
        scene.bind('mouseup', drop, cube) #Drop the cube man !!
def move(evt, obj):
    global drag_pos # The initial mouse position. 
    new_pos = scene.mouse.project(normal=(0,0,1))
    if new_pos != drag_pos: # if mouse has moved.  
        obj.pos += new_pos - drag_pos 
        drag_pos = new_pos 

def drop(evt):
    scene.unbind('mousemove', move)
    scene.unbind('mouseup', drop)

scene.bind('mousedown', take_obj)


## Créer des cubes pour les joueur 18 pour chaqu'un + attribution de couleurs ...
#def jeu(): 
##       nb_cubesJ1 = 18
#        nb_cubesJ2 = 18 # pour la machine du coup  
#        cubes_j1=[]
#        cubes_j2= []
#        for i in range(nb_cubesJ1):
#                BJ1 = box(size=TailleCube, color= color.cyan)
#                cubes_j1.append(BJ1)
#
#        for i in range(nb_cubesJ2):
#                BJ2 = box (size=TailleCube, color= color.green)
 #               cubes_j2.append(BJ2)
#jeu()