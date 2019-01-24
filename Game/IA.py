"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Pyramide
import Joueur
import Point

class IA:
    def __init__(self, joueur):
        self.py = Pyramide.Pyramide()
        self.j = joueur

    def choisir_piece(self, j, piece):
        for i in range(len(j.pions)):
            if j.pions[i].content == piece:
                return i
            pass
        pass
        if len(j.pions) == 0:
            return -1
        else:
            return 0
        pass

    def ajouter_point(self, etage, case):
        xmin = (case.x == 0)
        ymin = (case.y == 0)
        xmax = (case.x == len(self.py.plateau[i].etageArray[j])-1)
        ymax = (case.y == len(self.py.plateau[i].etageArray))
        if (xmin or xmax) and (ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y] += 0,3 #une arete
        elif (xmin or ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y] += 0,2 #un bord
        pass

    def has_triplet(py):
        for i in range(len(py.plateau)):
            for j in range(len(py.plateau[i].etageArray)):
                for k in range(len(py.plateau[i].etageArray[j])):
                    if (input.x+1 < len(self.py.plateau[etage].etageArray)):
                        if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                            case_d = self.py.plateau[etage].etageArray[input.x+1][input.y]
                            case_r = self.py.plateau[etage].etageArray[input.x][input.y+1]
                            if (case_d.content == case_r.content and case_d.content == self.j.pion):
                                self.py.ap
                            pass
                        pass
                        if (input.y > 0):
                            case_l = self.py.plateau[etage].etageArray[input.x][input.y-1]
                            case_ld = self.py.plateau[etage].etageArray[input.x+1][input.y-1]
                            if (case_l.content == case_ld.content and case_ld.content == self.j.pion):
                                has_triplet = 2
                            pass
                        pass
                    pass
                    if (input.x > 0):
                        if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                            case_u = self.py.plateau[etage].etageArray[input.x-1][input.y]
                            case_ur = self.py.plateau[etage].etageArray[input.x-1][input.y+1]
                            if (case_u.content == case_ur.content and case_u.content == self.j.pion):
                                has_triplet = 3
                            pass
                        pass
                    pass
                    if (etage == 0):
                        #best case
                    pass
                pass
            pass
        pass

    def evaluation_initiale(self, py):
        for i in range(len(self.plateau)):
            for j in range(len(self.py.plateau[i].etageArray)):
                for k in range(len(self.py.plateau[i].etageArray[j])):
                    self.ajouter_point(i, Point.Point(j, k))
                pass
            pass
        pass
        self.py.plateau[0].etageArray[0][0] += 1 #le sommet
