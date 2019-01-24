"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Etage
import Point

class Pyramide:

    def __call__(self):
        print("foo")

    def __init__(self):
        print("Initialisation du plateau")
        self.plateau = []
        for i in range(5):
            self.plateau.append(Etage.Etage(i))
        pass
        for j in self.plateau[4].etageArray:
            for i in j:
                i.content = 0
            pass
        pass
        #self.accessibles()
        #self.print_self()
        print("fin fin")

    def debloquer_etage(self):
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i].etageArray)):
                for k in range(len(self.plateau[i].etageArray[j])):
                    if ((j+1 < len(self.plateau[i].etageArray)) and (k+1 < len(self.plateau[i].etageArray[j]))):
                        case = self.plateau[i].etageArray[j][k]
                        case_d = self.plateau[i].etageArray[j+1][k]
                        case_r = self.plateau[i].etageArray[j][k+1]
                        if case_d.occupe() and case_r.occupe() and case.occupe():
                            if (i > 0) and (self.plateau[i-1].etageArray[j][k].content == 3):
                                self.plateau[i-1].etageArray[j][k].content = 0
                            pass
                        pass
                    pass
                pass
            pass
        pass

    def accessibles():
        print("accessibles :")
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i].etageArray)):
                for k in range(len(self.plateau[i].etageArray[j])):
                    if self.plateau[i].etageArray[j].content == 0:
                        print("Etage "+str(i)+": "+str(self.plateau[i].etageArray[j]))
                    pass
                pass
            pass
        pass
        print("fin accessibles")

    def __str__(self):
        sb = "Plateau :"
        for i in range(len(self.plateau)):
            sb += str(self.plateau[i])
        pass
        return sb

    """ obsolete -> pe
    def find_index(self, etage: int, point: Point) -> int:
        for lvl in self.plateau[etage]:
            for j in len(lvl):
            if Point.equals(lvl[j], point):
                return j
            pass
        pass
        return -1   """

    def get_pion(self, etage, point):
        return self.plateau[etage].etageArray[point.x][point.y]

    def set_pion(self, etage, point, etat):
        self.plateau[etage].etageArray[point.x][point.y].content = etat

    def pose(self, etage, input, pion):
        if not isinstance(input, Point.Point):
            raise TypeError
        print("Etage :"+str(etage)+", Point : ("+ str(input.x) + ", " + str(input.y) + ")")
        if self.get_pion(etage, input).is_ouvert():
            self.set_pion(etage, input, pion)
            return True
        else:
            return False
        pass
