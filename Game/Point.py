"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from math import *

class Point:

    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY
        self.content = 3 # 0 ouvert, 1 noir, 2 blanc
        self.refBox = box(pos=(0, 0, 0), size= vector(0,0,0), visible=False)

    def __str__(self):
        return str(self.content)

    def is_ouvert(self):
        return self.content == 0

    def equals(self, point):
        return (self.x == point.x and self.y == point.y)

    #si les contenus adjacents (certains pattern) sont egaux au pion
    def content_equals(self, point, pion):
        return self.content == pion and point.content == pion

    def occupe(self):
        return (self.content != 3) and (self.content != 0)
