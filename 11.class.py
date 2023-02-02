# 클래스 - 반복되는 것을 미리 설계
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdate(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def multi(self):
        result = self.first * self.second
        return result

    def divi(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def divi(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = MoreFourCal(4, 0)
print(a.add())
print(a.pow())
print(a.divi())
