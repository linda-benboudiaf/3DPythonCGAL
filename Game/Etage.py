"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Point

class Etage:
    def __init__(self, inputNiveau):
        self.niveau = inputNiveau # genre python peut pas faire de i <= x
        self.etageArray = []
        for ix in range(self.niveau+1):
            self.etageArray.append([])
            for iy in range(self.niveau+1):
                if ix+iy <= self.niveau:
                    newPoint = Point.Point(ix,iy)
                    self.etageArray[ix].append(newPoint)
                pass
            pass
        pass

    def __str__(self):
        sb = "Etage " + str(self.niveau) + "\n"
        for i in range(len(self.etageArray)):
            for j in self.etageArray[i]:
                sb += str(j)
            pass
            sb += "\n"
        pass
        return sb
