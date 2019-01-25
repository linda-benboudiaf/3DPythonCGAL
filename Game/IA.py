"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Pyramide
import Joueur
import Point
import random
#l'IA attribue une note sur 10 hahahahahaha
class IA(Joueur.Joueur):
    def __init__(self, pion, name):
        self.py = Pyramide.Pyramide()
        self.piece = pion
        self.name = name
        self.pion = pion
        self.pions = []
        if (pion == 1):
            self.init_pions(1, 2)
        else:
            self.init_pions(2, 1)
        pass

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

    def predict(self, py):
        random.seed(a = None)
        self.py.reinitialiser()
        self.evaluation_initiale(py)
        self.parcourt_triplet(py)
        cases = []
        max = -1
        for i in range(len(self.py.plateau)):
            for j in range(len(self.py.plateau[i].etageArray)):
                for k in range(len(self.py.plateau[i].etageArray[j])):
                    if self.py.plateau[i].etageArray[j][k].content == max:
                        cases.append([i, Point.Point(j, k)])
                    elif self.py.plateau[i].etageArray[j][k].content > max:
                        cases = []
                        cases.append([i, Point.Point(j, k)])
                        max = self.py.plateau[i].etageArray[j][k].content
                    pass
                pass
            pass
        pass
        return random.choice(cases)

    def ajouter_point(self, etage, x, case):
        xmin = (case.x == 0)
        ymin = (case.y == 0)
        xmax = (case.x == len(self.py.plateau[etage].etageArray)-1)
        ymax = (case.y == len(self.py.plateau[etage].etageArray[x])-1)
        if (xmin or xmax) and (ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y].content += 5 #une arete
        elif (xmin or ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y].content += 4 #un bord
        pass

    def parcourt_triplet(self, py):
        for i in range(len(py.plateau)):
            for j in range(len(py.plateau[i].etageArray)):
                for k in range(len(py.plateau[i].etageArray[j])):
                    if (py.plateau[i].etageArray[j][k].is_ouvert()):
                        self.triplet(py, i, Point.Point(j, k))
                    elif (py.plateau[i].etageArray[j][k].content == self.pion):
                        self.adjacence(i, py, Point.Point(j, k))
                        self.py.plateau[i].etageArray[j][k].content = -1
                    else:
                        self.py.plateau[i].etageArray[j][k].content = -1
                    pass
                pass
            pass
        pass

    def adjacence(self, etage, py, case):
        xmin = (case.x > 0)
        ymin = (case.y > 0)
        xmax = (case.x+1 < len(self.py.plateau[etage].etageArray))
        if xmin:
            if ymin:
                if (py.get_pion(etage, Point.Point(case.x-1, case.y-1)).is_ouvert()):
                    self.py.plateau[etage].etageArray[case.x-1][case.y-1].content += 1
                pass
            pass
            if (case.y+1 < len(self.py.plateau[etage].etageArray[case.x-1])):
                if (py.get_pion(etage, Point.Point(case.x-1, case.y+1)).is_ouvert()):
                    self.py.plateau[etage].etageArray[case.x-1][case.y+1].content += 1
                pass
            pass
            if (py.get_pion(etage, Point.Point(case.x-1, case.y)).is_ouvert()):
                self.py.plateau[etage].etageArray[case.x-1][case.y].content += 1
            pass
        pass
        if xmax:
            if ymin:
                if (py.get_pion(etage, Point.Point(case.x+1, case.y-1)).is_ouvert()):
                    self.py.plateau[etage].etageArray[case.x+1][case.y-1].content += 1
                pass
            pass
            if (case.y+1 < len(self.py.plateau[etage].etageArray[case.x+1])):
                if (py.get_pion(etage, Point.Point(case.x+1, case.y+1)).is_ouvert()):
                    self.py.plateau[etage].etageArray[case.x+1][case.y+1].content += 1
                pass
            pass
            if (case.y < len(self.py.plateau[etage].etageArray[case.x+1])):
                if (py.get_pion(etage, Point.Point(case.x+1, case.y)).is_ouvert()):
                    self.py.plateau[etage].etageArray[case.x+1][case.y].content += 1
                pass
            pass
        pass
        if ymin:
            if (py.get_pion(etage, Point.Point(case.x, case.y-1)).is_ouvert()):
                self.py.plateau[etage].etageArray[case.x][case.y-1].content += 1
            pass
        pass
        if (case.y+1 < len(self.py.plateau[etage].etageArray[case.x])):
            if (py.get_pion(etage, Point.Point(case.x, case.y+1)).is_ouvert()):
                self.py.plateau[etage].etageArray[case.x][case.y+1].content += 1
            pass
        pass

    def triplet(self, py, etage, input):
        if (input.x+1 < len(self.py.plateau[etage].etageArray)):
            if (input.y+1 < len(py.plateau[etage].etageArray[input.x])):
                case_d = py.plateau[etage].etageArray[input.x+1][input.y]
                case_r = py.plateau[etage].etageArray[input.x][input.y+1]
                if (case_d.content == case_r.content):
                    if (case_d.content == self.pion):
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 7
                    elif (case_d.occupe()): #case adverse haha
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 5
                    pass
                pass
            pass
            if (input.y > 0):
                case_l = py.plateau[etage].etageArray[input.x][input.y-1]
                case_ld = py.plateau[etage].etageArray[input.x+1][input.y-1]
                if (case_l.content == case_ld.content):
                    if (case_ld.content == self.pion):
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 7
                    elif (case_l.occupe()): #case adverse haha
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 5
                    pass
                pass
            pass
        pass
        if (input.x > 0):
            if (input.y+1 < len(py.plateau[etage].etageArray[input.x])):
                case_u = py.plateau[etage].etageArray[input.x-1][input.y]
                case_ur = py.plateau[etage].etageArray[input.x-1][input.y+1]
                if (case_u.content == case_ur.content):
                    if (case_u.content == self.pion):
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 7
                    elif (case_u.occupe()): #case adverse haha
                        self.py.plateau[etage].etageArray[input.x][input.y].content += 5
                    pass
                pass
            pass
        pass

    def evaluation_initiale(self, py):
        for i in range(len(self.py.plateau)):
            for j in range(len(self.py.plateau[i].etageArray)):
                for k in range(len(self.py.plateau[i].etageArray[j])):
                    self.ajouter_point(i, j, Point.Point(j, k))
                pass
            pass
        pass
        self.py.plateau[0].etageArray[0][0].content += 20 #le sommet tant convoit"et" -nonASCII
