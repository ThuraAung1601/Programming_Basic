class Fraction:
    def __init__(self,num,denum):
        self.num = num
        self.denum = denum
    def __str__(self):
        return str(self.num) + "/" + str(self.denum)
    def __add__(self,other):
        top = self.num * other.denum + other.num * self.denum
        bott = self.denum * other.denum
        return Fraction(top,bott)
    def __float__(self):
        return self.num / self.denum

a = Fraction(1,4)
b = Fraction(3,5)
c = a + b
print(a)
print(float(a))
print(b)
print(c)
print(float(c))