class TVector:
    def __init__(self, *args):
        self.matrix = list(map(float, args))

    @property
    def len(self):
        return len(self.matrix)

    def parallel(self, other):
        k = self.matrix[0] / other.matrix[0]
        for i in range(1, self.len):
            if self.matrix[i] / other.matrix[i] != k:
                return False
        return True

    def perpendicularity(self, other):
        d = 0
        for i in range(self.len):
            d += self.matrix[i] * other.matrix[i]
        return True if d == 0 else False

    def length(self):
        return (sum([el**2 for el in self.matrix]))**0.5

    def __iadd__(self, other):
        return self.length() + other


class TVector2(TVector):
    def __init__(self, x, y):
        super().__init__(x, y)


class TVector3(TVector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


f = [TVector3(1, 2, 3), TVector2(1, 2), TVector3(2, 4, 6), TVector2(2, 4), TVector2(0, 23), TVector3(14, 14, 1),
     TVector3(4, 4, 1)]

for i in range(7):
    if type(f[i]) == TVector2:
        f_k_2 = f[i]
        break

for i in range(7):
    if type(f[i]) == TVector3:
        f_k_3 = f[i]
        break

f2 = sum([el.length() for el in f if type(el) == TVector2 and el.parallel(f_k_2)])
f3 = sum([el.length() for el in f if type(el) == TVector3 and el.parallel(f_k_3)])
print('sum vector 2 = {0}\nsum vector 3 = {1}'.format(f2, f3))
