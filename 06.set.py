s1 = {1,2,3,4,5}
s2 = set([4,5,6,7,8])

# 출력
print(s1)
print(s2)

# 중복 제거로 set화
a = [1,1,1,2,2,2,2,2,3,3,3]
print(a)
newA = list(set(a))
print(newA)

# 문자열 set
s3 = set("Kim J W")
print(s3)

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 값 1개 추가
s1.add(9)
print(s1)
# 값 여러 개 추가
s2.update([100,100,111])
print(s2)

# 값 제거
s2.remove(111)
print(s2)