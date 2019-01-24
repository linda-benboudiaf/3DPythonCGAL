"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Pyramide
import Joueur
import Point

class Jeu:

    def __call__(self):
        print("foo")

    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        self.py = Pyramide.Pyramide()

    def choisir_piece(self, j):
        print(j)
        p = input("numero pion? : ")
        idx_pion = int(p)
        if j.is_pion_available(idx_pion):
            return j.pions.pop(idx_pion)
        else:
            return self.choisir_piece_adv(j)
        pass

    def verifier_inputs(etage, input):
        return (input.x < etage+1) and (input.x >= 0) and (input.y < etage+1) and (input.y >= 0) and (etage >= 0) and (etage < 5)

    def passerTour(self, j, finish):
        in1 = input("etage? : ")
        etage = int(in1)
        in2 = input("y? : ") #le sens des axes, c'est complique. Stop juger
        x = int(in2)
        in3 = input("x? : ")
        y = int(in3)
        input4 = Point.Point(x, y)
        if (not Jeu.verifier_inputs(etage, input4)):
            print("mauvais input")
            self.passerTour(j, False)
        pass
        pion = self.choisir_piece(j)
        if (not self.py.pose(etage, input4, pion)):
            print("place non disponible")
            self.passerTour(j, False)
        pass
        self.py.debloquer_etage()
        print(self.py)
        self.tour_supplementaire(j, etage, input4, pion)

    def tour_supplementaire(self, j, etage, input4, pion):
        rejouer = self.rejouer(j, etage, input4, pion)
        if (rejouer > 0 and not finish):
            pion = self.choisir_piece(self.swap_j(j))
            if (rejouer == 1):
                self.py.pose(etage-1, input4, pion)
            pass
            if (rejouer == 2):
                self.py.pose(etage-1, Point.Point(input4.x, input4.y-1), pion)
            pass
            if (rejouer == 3):
                self.py.pose(etage-1, Point.Point(input4.x-1, input4.y), pion)
            pass
            self.py.debloquer_etage()
            print(self.py)

    def is_finish(self):
        return (len(self.j1.pions) == 0) or (len(self.j2.pions) == 0)

    def is_really_finish(self, j):
        return len(j.pions) == 0

    def jouer(self):
        j = self.j1
        print(self.py)
        while (not self.is_finish()):
            self.passerTour(j, False)
            j = self.swap_j(j)
        pass
        if (len(self.j1.pions) == 0):
            j = self.j2
        else:
            j = self.j1
        pass
        while (not self.is_really_finish(j)):
            self.passerTour(j, True)
        pass
        print(self.compter_points())

    def qui_gagne(acc1, acc2):
        if acc1 > acc2:
            return 1
        if acc1 < acc2:
            return -1
        else:
            return 0

    def compter_points(self):
        acc = 0
        acc_j1 = 0
        acc_j2 = 0

        #une face parcourue haut
        for i in range(len(self.py.plateau)):
            for k in range(len(self.py.plateau[i].etageArray[0])):
                if (self.py.plateau[i].etageArray[0][k].content == self.j1.pion):
                    acc_j1 += 1
                else:
                    acc_j2 += 1
                pass
            pass
        pass
        acc += qui_gagne(acc_j1, acc_j2)

        #2eme face gauche
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i].etageArray)):
                if (self.plateau[i].etageArray[j][0].content == self.j1.pion):
                    acc_j1 += 1
                else:
                    acc_j2 += 1
                pass
            pass
        pass
        acc += qui_gagne(acc_j1, acc_j2)

        #3eme face
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i].etageArray)):
                if (self.plateau[i].etageArray[j][len(self.plateau[i].etageArray[j])-1].content == self.j1.pion):
                    acc_j1 += 1
                else:
                    acc_j2 += 1
                pass
            pass
        pass
        acc += qui_gagne(acc_j1, acc_j2)
        if acc > 0:
            return "gg j1"
        if acc < 0:
            return "gg j2"
        else:
            return "match nul"


    def rejouer(self, j, etage, input, pion):
        has_triplet = -1
        if j.pion == pion:
            if (input.x+1 < len(self.py.plateau[etage].etageArray)):
                if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                    case_d = self.py.plateau[etage].etageArray[input.x+1][input.y]
                    case_r = self.py.plateau[etage].etageArray[input.x][input.y+1]
                    if (case_d.content == case_r.content and case_d.content == pion):
                        has_triplet = 1
                    pass
                pass
                if (input.y > 0):
                    case_l = self.py.plateau[etage].etageArray[input.x][input.y-1]
                    case_ld = self.py.plateau[etage].etageArray[input.x+1][input.y-1]
                    if (case_l.content == case_ld.content and case_ld.content == pion):
                        has_triplet = 2
                    pass
                pass
            pass
            if (input.x > 0):
                if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                    case_u = self.py.plateau[etage].etageArray[input.x-1][input.y]
                    case_ur = self.py.plateau[etage].etageArray[input.x-1][input.y+1]
                    if (case_u.content == case_ur.content and case_u.content == pion):
                        has_triplet = 3
                    pass
                pass
            pass
        pass
        return has_triplet

    def swap_j(self, j) :
        if (j == self.j1):
            return self.j2
        else:
            return self.j1
        pass
