# 숫자형
a = 1
print(type(a))

b = 1.23
print(type(b))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b**b)
# 몫
print(a//b)
# 나머지
print(a%b)

# 문자형
c = "Python's favorite food is apple."
print(c)
d = 'Python\'s favorite food is apple.'
print(d)
e = 'Life is tpp short\nYou need python'
print(e)
f = """Life
id
My Life!"""
print(f)
g = 'a+'
print(g*4)

# 문자열 인덱싱
print(c[3])
print(c[-3])
# 슬라이싱 : a[이상:미만:간격]
print(c[9:17])
print(c[9:17:2])

h = '123456789'
print(h[::2])
print(h[::-2])

# 문자열 포맷팅
i = "I eat %d apples." % 3
number = 7
day = 'three'
j = "I ate %d apples. So I was sick for %s days." % (number, day)
print(i)
print(j)

# %s = 문자열
# %c = 문자 1개
# %d = 정수
# %f = 부동 소수
# %% = %자체

k = "asdfsadf sdfs fsd fsdf {} sfdsfsdf".format("안녕")
kk = "asdfsad {age} f sdfs fsd fsdf {name} sfdsfsdf".format(name="김주원", age="37")
print(k)
print(kk)

new_name = "인트"
kkk = f"나의 이름은 {new_name}입니다."
print(kkk)

# 공백처리
l = "%10s" % "hi"
print(l)

# 소수점 자리 정하기
ll = "%0.2f" % 3.14254363453
print(ll)

#문자열 갯수 세기
m = 'hobby'
print(m.count('h'))

# 위치 알려주기 - 있으면 그 위치값 , 없으면 -1 출력
print(j.find('t'))
print(j.index('t'))

# 조인, 앞의 문자열을 사이에 넣기
o = ",".join("happy")
print(o)
oo = ",".join(["a","b","c"])
print(oo)

# 대문자로 만들기
p = ' hi Opp S '
print(p.upper())
# 소문자 만들기
print(p.lower())

# 양쪽 공백 지우기
print(p.strip())

# 문자열 바꾸기
print(p.replace("hi", "Hello"))

#문자열 나누기 -> 리스트로 만들어줌
print(p.split())
pp = 'a, b, c, d, e'
print(pp.split(','))

# 참조값 주소 알기
print(id(pp))
# 같은 주소인지 확인
print(a is b)

# 변수 할당법
aa, bb = (1,2)
(cc, dd) = (3, 5)
ee, ff = 'python', 'life'
[gg,hh] = ['apple', 'gal']
ii = jj = 34
print(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)

# 값 서로 바꾸기
aaa = 3
bbb = 5
print(aaa,bbb)
aaa,bbb = bbb,aaa
print(aaa,bbb)