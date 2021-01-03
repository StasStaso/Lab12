from math import sqrt, cos, sin


class TPolyangle:
    def __init__(self, *args):
        self.__sides = list(args)

    def s(self):
        l = len(self.__sides)
        if l == 0 or l == 2:
            return 0
        elif l == 3:
            p = sum(self.__sides) / 2
            return sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
        elif l == 4:
            p = sum(self.__sides) / 2
            return sqrt(
                p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]) * (p - self.__sides[3]))
        else:
            return (l * (self.__sides[0] ** 2) / 4) * ((cos(180 / l) / sin(180 / l)))

    def p(self):
        return sum(self.__sides)

    def __getitem__(self, index):
        return self.__sides[index]

    def __setitem__(self, key, value):
        if key >= 0 and value >= 0:
            self.__sides[key] = value

    def __delitem__(self, key):
        del self.__sides[key]


obj = TPolyangle(2,3,4)
print("S = ",obj.s())
print("P = ",obj.p())
print("Obj[1] = ",obj[1])
