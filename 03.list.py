a = ["kim jw", "jung hm", ["moon sh", "kim ih"], "kim jy"]
print(a)
print(a[1])
print(a[2])
print(a[2][0])
# 슬라이싱
print(a[1:3])

# 리스트 더하기
aa = ["jo jj", ["adf dfae", "age ee"], "rti msm"]
print(a+aa)
# 리스트 곱 (반복)
print(a*3) 

#리스트 바꾸기
a[3] = "kimu jy"
print(a)
# 리스트 삭제
a[2:3] = []
print(a)
del a[2]
print(a)
# 가장 먼저 걸리는거만 삭제
a.remove("kim jw")
print(a)

# 리스트헝 함수
# 1. 추가
a.append("moon sh")
print(a)
# 2. 특정 위치에 추가 
a.insert(1,"kim ih")
# 3. 여러 개 넣기 - 확장
a.extend(["kim kw", "fds soso"])
print(a)

# 정렬 오름차순
a.sort()
print(a)
# 배열 순서 바꾸기
a.reverse()
print(a)

# 있으면 인덱스 출력
print(a.index("kim ih"))

# 리스트 끄집어내기 - 안에 없으면 마지막 빠짐
b = [1,2,3,4,5,1,6]
print(b.pop())
print(b)
print(b.pop(2))

# 갯수 세기
print(b.count(1))

# 진짜 리스트 복사
x = [1,2,3]
y = x[::]
print(x)
print(y)
print(id(x))
print(id(y))
print( x is y)

from copy import copy
x = [1,2,3,4]
y = copy(x)
print(x)
print(y)