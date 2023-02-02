def sum(a, b):
    result = a + b
    return result


def say():
    return 'hi'


def hap(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


print(sum(10, 20))
print(say())
print(hap(5, 8))

# 여러 개 입력값 함수


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 23, 4, 5, 8))


# 키워드 여러 개 (디셔너리 같은거)


def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if (k == "name"):
            print("당신의 이름은 : " + kwargs[k])


print(print_kwargs(name="kyo husanaji", b="dd"))


# 함수의 리턴값은 하나
def sum_and_mul(a, b):
    return a+b, a*b


print(sum_and_mul(2, 3))
print(sum_and_mul(2, 3)[0])


# 초기값 미리 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


print(say_myself('Honjiji', 32, False))

# 지역변수와 글로벌변수
a = 1


def vartest():
    global a
    a = a+1


vartest()
print(a)

# lambda = 함수 간단하게 표현


def add(a, b): return a+b


myApp = [lambda a, b: a*b, lambda a, b: a/b]

print(myApp[0](3, 5))
print(myApp[1](3, 5))
