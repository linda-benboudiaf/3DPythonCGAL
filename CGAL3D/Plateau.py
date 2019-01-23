# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from math import *

# Mettre en place Camèra + Lumière ...
# Scene represente le monde "World" on definit certain paramètre initial... 
scene = display(x=0, y=0, z=0, width= 800, height=900, center=(1,0,0),title = 'Plateau.Inside', background=(1, 1, 1))
scene.range = 5
scene.autocenter = True
# Lumière 
local_light(pos=(-10,-10,10), color=color.yellow)

#Premier niveau un pion possible 
b1= box(pos=(0, 4,2), size=(2,2,2))
b1Bis= box(pos=(0,4,0), size=(2,2,2))
b2= box (pos=(2,2,2), size=(2,2,2))
b2Bis= box (pos=(2,2,0), size=(2,2,2))
b3= box(pos=(0,2,2), size=(2,2,2)) # Pas de cube jumelle 
#Deuxieme Niveau 
b4= box(pos=(0,6,0), size=(2,2,2))
b4Bis = box(pos=(0,6,-2), size=(2,2,2))
b5= box(pos=(2,4,0), size=(2,2,2))
b5Bis = box(pos=(2,4,-2), size=(2,2,2))
b6= box(pos=(4,2,0), size=(2,2,2))
b6Bis= box(pos=(4,2,-2), size=(2,2,2))
#Vu arrière du plateau #Troisième niveau
b7= box(pos=(0,8,-2), size=(2,2,2))
b7Bis= box(pos=(0,8,-4), size=(2,2,2))
b8= box(pos=(2,6,-2), size=(2,2,2))
b8Bis= box(pos=(2,6,-4), size=(2,2,2))
b9= box(pos=(4,4,-2), size=(2,2,2))
b9Bis= box(pos=(4,4,-4), size=(2,2,2))
b10= box(pos=(6,2,-2), size=(2,2,2))
b10Bis = box(pos=(6,2,-4), size=(2,2,2))
# Quatième Niveau vu arrière 
b11= box(pos=(0,10,-4),size=(2,2,2))
b11Bis = box(pos=(0,10,-6),size=(2,2,2))
b12= box(pos=(2,8,-4), size=(2,2,2))
b12Bis= box(pos=(2,8,-6), size=(2,2,2))
b13= box(pos=(4,6,-4), size=(2,2,2))
b13Bis= box(pos=(4,6,-6), size=(2,2,2))
b14= box(pos=(6,4,-4), size=(2,2,2))
b14Bis= box(pos=(6,4,-6), size=(2,2,2))
b15= box(pos=(8,2,-4), size=(2,2,2))
b15Bis= box(pos=(8,2,-6), size=(2,2,2))
# Dernier niveau
b16= box(pos=(0,12,-6), size=(2,2,2))
b17= box(pos=(2,10,-6), size=(2,2,2))
b18= box(pos=(4,8,-6), size=(2,2,2))
b19= box(pos=(6,6,-6), size=(2,2,2))
b20= box(pos=(8,4,-6), size=(2,2,2))
b21= box(pos=(10,2,-6), size=(2,2,2))

# Pied du Plateau ...
b22= box(pos=(0,12,-8), size=(2,2,2))
b22Bis= box(pos=(2,12,-8), size=(2,2,2))
b23= box(pos=(4,10,-8), size=(2,2,2))
b23Bis= box(pos=(2,10,-8), size=(2,2,2))
b24= box(pos=(6,8,-8), size=(2,2,2))
b24Bis= box(pos=(4,8,-8), size=(2,2,2))
b25= box(pos=(8,6,-8), size=(2,2,2))
b25Bis= box(pos=(6,6,-8), size=(2,2,2))
b26= box(pos=(10,4,-8), size=(2,2,2))
b26Bis= box(pos=(8,4,-8), size=(2,2,2))
b27= box(pos=(10,2,-8), size=(2,2,2))

# Définition de la couleur du plateau (Des cubes quoi !!)
CouleurChoco = vector(86.7,39.26,17.69)
for cube in scene.objects:
    if isinstance(cube, box):
        cube.color = vector(1,0.5, 1)
        
# Drag and Drop du Cube
cube = box(pos=(10, -10,0), size=(2,2,2),color= color.yellow)
n = 18
#for i in range(n):
    #cube = box(pos=(0, 0,0), size=(2,2,2),color= color.yellow)

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
