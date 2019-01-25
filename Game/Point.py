"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
class Point:

    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY
        self.content = 3 # 0 ouvert, 1 noir, 2 blanc
        self.ref = -1

    def __str__(self):
        return str(self.content)

    def set_ref(self, ref):
        self.ref = ref
        
    def is_ouvert(self):
        return self.content == 0

    def equals(self, point):
        return (self.x == point.x and self.y == point.y)

    #si les contenus adjacents (certains pattern) sont egaux au pion
    def content_equals(self, point, pion):
        return self.content == pion and point.content == pion

    def occupe(self):
        return (self.content != 3) and (self.content != 0)
