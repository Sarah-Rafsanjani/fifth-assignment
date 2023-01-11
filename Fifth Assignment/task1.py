class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat, "/", self.makhraj)

    def mul(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.soorat
        result.makhraj = self.makhraj * f2.makhraj
        return result
    
    def add(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj + self.makhraj * f2.soorat
        result.makhraj = self.makhraj * f2.makhraj
        return result
    
    def sub(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj - self.makhraj * f2.soorat
        result.makhraj = self.makhraj * f2.makhraj
        return result

    def div(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj
        result.makhraj = self.makhraj * f2.soorat
        return result   
    
s1 = int(input("Enter the numerator of the first fraction: "))
m1 = int(input("Enter the denominator of the first fraction: "))
fraction1 = Fraction(s1, m1)
fraction1.show()

s2 = int(input("Enter the numerator of the second fraction: "))
m2 = int(input("Enter the denominator of the second fraction: "))
fraction2 = Fraction(s2, m2)
fraction2.show()

print("Here are multiplication, addition, subtraction and division, respectively:")
m = fraction1.mul(fraction2)
m.show()
a = fraction1.add(fraction2)
a.show()
s = fraction1.sub(fraction2)
s.show()
d = fraction1.div(fraction2)
d.show()