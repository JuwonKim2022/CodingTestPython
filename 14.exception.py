try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("안녕하세요")

try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

g = open('fooo.txt', 'w')
try:
    data = g.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()

# 오류 발생시킴


class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
