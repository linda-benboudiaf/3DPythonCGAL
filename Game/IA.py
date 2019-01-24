"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Pyramide
import Joueur
import Point

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
                    pass
                pass
            pass
        pass
        return random.choice(cases)


    def ajouter_point(self, etage, x, case):
        xmin = (case.x == 0)
        ymin = (case.y == 0)
        xmax = (case.x == len(self.py.plateau[etage].etageArray)-1)
        ymax = (case.y == len(self.py.plateau[etage].etageArray[x]))
        if (xmin or xmax) and (ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y].content += 3 #une arete
        elif (xmin or ymin or ymax):
            self.py.plateau[etage].etageArray[case.x][case.y].content += 2 #un bord
        pass

    def parcourt_triplet(self, py):
        for i in range(len(py.plateau)):
            for j in range(len(py.plateau[i].etageArray)):
                for k in range(len(py.plateau[i].etageArray[j])):
                    if (py.plateau[i].etageArray[j][k].is_ouvert()):
                        self.triplet(py, i, Point.Point(j, k))
                    else:
                        self.py.plateau[i].etageArray[j][k] = -1
                    pass
                pass
            pass
        pass

    def triplet(self, py, etage, input):
        if (input.x+1 < len(self.py.plateau[etage].etageArray)):
            if (input.y+1 < len(py.plateau[etage].etageArray[input.x])):
                case_d = py.plateau[etage].etageArray[input.x+1][input.y]
                case_r = py.plateau[etage].etageArray[input.x][input.y+1]
                if (case_d.content == case_r.content and case_d.content == self.pion):
                    self.py.plateau[etage].etageArray[case.x][case.y].content += 5
                pass
            pass
            if (input.y > 0):
                case_l = py.plateau[etage].etageArray[input.x][input.y-1]
                case_ld = py.plateau[etage].etageArray[input.x+1][input.y-1]
                print(case_l, case_ld)
                if (case_l.content == case_ld.content and case_ld.content == self.pion):
                    self.py.plateau[etage].etageArray[case.x][case.y].content += 5
                pass
            pass
        pass
        if (input.x > 0):
            if (input.y+1 < len(py.plateau[etage].etageArray[input.x])):
                case_u = py.plateau[etage].etageArray[input.x-1][input.y]
                case_ur = py.plateau[etage].etageArray[input.x-1][input.y+1]
                if (case_u.content == case_ur.content and case_u.content == self.pion):
                    self.py.plateau[etage].etageArray[case.x][case.y].content += 5
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
        self.py.plateau[0].etageArray[0][0].content += 10 #le sommet
