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

    def passerTour(self, j):
        adv = self.swap_j(j)
        print(adv)
        p = input("numero pion? : ")
        idx_pion = int(p)
        if adv.is_pion_available(idx_pion):
            pion = adv.pions.pop(idx_pion)
        else:
            self.passerTour(j)
        pass
        in1 = input("etage? : ")
        etage = int(in1)
        in2 = input("x? : ")
        x = int(in2)
        in3 = input("y? : ")
        y = int(in3)
        input4 = Point.Point(x, y)
        if (not self.py.pose(etage, input4, pion)):
            self.passerTour(j)
        pass
        self.py.debloquer_etage()
        print(self.py)
        if (self.rejouer(j, etage, input4)):
            print("rejouer")
            self.passerTour(j)
        pass

    def is_finish(self):
        return (len(self.j1.pions) == 0) and (len(self.j2.pions) == 0)

    def jouer(self):
        j = self.j1
        while (not self.is_finish()):
            self.passerTour(j)
            j = self.swap_j(j)
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


    def rejouer(self, j, etage, input):
        has_triplet = False
        if (input.x+1 < len(self.py.plateau[etage].etageArray)):
            if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                case_d = self.py.plateau[etage].etageArray[input.x+1][input.y]
                case_r = self.py.plateau[etage].etageArray[input.x][input.y+1]
                print(case_d.content, case_r.content, j.pion)
                has_triplet = case_d.content_equals(case_r, j.pion)
            pass
            if (input.y > 0):
                case_u = self.py.plateau[etage].etageArray[input.x][input.y-1]
                case_ur = self.py.plateau[etage].etageArray[input.x+1][input.y-1]
                print(case_u.content, case_ur.content, j.pion)
                has_triplet = has_triplet or case_u.content_equals(case_ur, j.pion)
            pass
        pass
        if (input.x > 0):
            if (input.y+1 < len(self.py.plateau[etage].etageArray[input.x])):
                case_l = self.py.plateau[etage].etageArray[input.x-1][input.y]
                case_ld = self.py.plateau[etage].etageArray[input.x-1][input.y+1]
                print(case_l.content, case_ld.content, j.pion)
                has_triplet = has_triplet or case_l.content_equals(case_ld, j.pion)
            pass
        pass
        return has_triplet

    def swap_j(self, j) :
        if (j == self.j1):
            return self.j2
        else:
            return self.j1
        pass
