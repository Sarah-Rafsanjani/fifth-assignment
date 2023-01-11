class Time:
    def __init__(self, h, m, s):
        self. h = h
        self. m = m
        self. s = s 

    def show(self):
        print(self.h, ":", self.m, ":", self.s)

    def add(self, t2):
        result = Time(None, None, None)
        result.h = self.h + t2.h
        result.m = self.m + t2.m
        result.s = self.s + t2.s
        if result.s >= 60:
            result.s -= 60
            result.m += 1
        if result.m >= 60:
            result.m -= 60
            result.h += 1
        return result
    
    def sub(self, t2):
        result = Time(None, None, None)
        result.h = self.h - t2.h
        result.m = self.m - t2.m
        result.s = self.s - t2.s
        if result.m < 0:
            result.h -= 1
            result.m += 60
        if result.s < 0:
            result.m -= 1
            result.s += 60
        return result

    def ttos(self):
        result = self.h * 3600 + self.m * 60 + self.s
        print(result)

    def stot(self):
        result = Time(None, None, None)
        self.h = int(self//3600)
        self.m = int(self//60 - (self//3600))
        self.s = int(self - (self//60) - (self//3600))
        return result


time1 = Time(18, 30, 40)
print("Time 1:")
time1.show()
time2 = Time(15, 45, 30)
print("Time 2:")
time2.show()
seconds = int(input("Enter the number of seconds: "))

print("addition")
a = time1.add(time2)
a.show()

print("subtraction")
s = time1.sub(time2)
s.show()

print("Time 1 to seconds")
ts1 = time1.ttos()

print("Time 2 to seconds")
ts2 = time2.ttos()

print("Seconds to time: (6850)")
st1 = seconds.stot()
st1.show()