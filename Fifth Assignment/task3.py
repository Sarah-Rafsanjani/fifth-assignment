class Date:
    def __init__(self, y, m, d):
        self. y = y
        self. m = m
        self. d = d 

    def show(self):
        print(self.y, "/", self.m, "/", self.d)

    def add(self, date2):
        result = Date(None, None, None)
        result.y = self.y + date2.y
        result.m = self.m + date2.m
        result.d = self.d + date2.d
        if result.d > 30:
            result.d -= 30
            result.m += 1
        if result.m > 12:
            result.m -= 12
            result.y += 1
        return result
    
    def sub(self, date2):
        result = Date(None, None, None)
        result.y = self.y - date2.y
        result.m = self.m - date2.m
        result.d = self.d - date2.d
        if result.d < 0:
            result.m -= 1
            result.d += 30
        if result.m < 0:
            result.y -= 1
            result.m += 12
        return result

    def getmonthname(self):
        if self.m == 1:
            result = "فروردین"
        if self.m == 2:
            result = "اردیبهشت"
        if self.m == 3:
            result = "خرداد"  
        if self.m == 4:
            result = "تیر"
        if self.m == 5:
            result = "مرداد"
        if self.m == 6:
            result = "شهریور"
        if self.m == 7:
            result = "مهر"
        if self.m == 8:
            result = "آبان"
        if self.m == 9:
            result = "آذر"
        if self.m == 10:
            result = "دی"
        if self.m == 11:
            result = "بهمن"
        if self.m == 12:
            result = "اسفند"
        print(result)

    def IsValidDate(self):
        if 1 <= self.y <= 9999 and 1 <= self.m <= 12 and 1 <= self.d <= 30:
            print("True")
        else:
            print("False")

print("date1: ")
date1 = Date(1358,2, 12)
date1.show()
print("date2: ")
date2 = Date(1380,11, 28)
date2.show()

print("this is the addition of the dates:")
a = date1.add(date2)
a.show()

print("this is the subtraction of the dates:")
s = date1.sub(date2)
s.show()

print("this is the month of each date: ")
gmn1 = date1.getmonthname()
gmn2 = date2.getmonthname()

print("this is the validation of two dates in order.")
valid1 = date1.IsValidDate()
valid2 = date2.IsValidDate()