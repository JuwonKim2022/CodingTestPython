print('1. 포맷')
# 금액표시
a = format(10000000, ',')
print(a)
# 8진수
a = format(10000000, 'e')
print(a)
# 16진수
a = format(10000000, 'x')
print(a)
# 느낌표를 채울건데, 오른쪽에 맞춰서 부호표시(0,-),20자리에 맞추어 출력, 콤마찍고, 소수점 4자리까지출력
a = format(1000, '!>020,.4f')
print(a)
print()

print('2. 필터 사용법')


def kim(value):
    if value % 2 == 0:
        return True
    else:
        return False


b = filter(kim, range(20))  # 참조변수만 나옴
print(b)
b = list(filter(kim, range(20)))  # 리스트로 값 출력
print(b)
print()

print('3. 람다 및 필터 사용')

b = list(filter(lambda x: x % 2 == 0, range(20)))
print(b)
print()

print('4. 삼항 연산자')
b = [i for i in range(20) if i % 2 == 0]
print(b)
b = list(i for i in range(20) if i % 2 == 0)
print(b)
print()

print('5. len')
# 리스트 길이 출력
c = len([1, 2, 3, 4])
print(c)
print()

print('6. map과 zip')
# map
c = list(map(lambda x: x**2, range(20)))
print(c)
# zip
c = list(zip(['a', 'b', 'c'], [1, 2, 3], [10, 20, 30], 'Ab!'))
print(c)
print()

print('7. max & min')
listA = [1, 2, 3, 4]
# max
d = max(listA)
print(d)
# min
d = min(listA)
print(d)
print()

print('8. sorted & sort')
listB = [10, 5, 4, 3, 7, 6]

# sorted - 배열을 직접 만지지 않음
new_list = sorted(listB)
print(new_list)
print(listB)

# sorted는 정렬할 때 유리
test_one = ['abc', 'def', 'hello world', 'python']
e = sorted(test_one, key=len, reverse=True)
print(e)

test_two = 'Life is too short, You need python'.split()
e = sorted(test_two, key=str.lower)
print(e)

test_three = list(zip('anvfe', [1, 2, 5, 4, 3]))
print(test_three)
f = sorted(test_three, key=lambda x: x[1])
print(f)
g = sorted(test_three, key=lambda x: x[0])
print(g)
# sort - 배열을 직접 만짐
listC = [1, 2, 5432, 7, 23, 3]
listC.sort()
print(listC)
print()

print('9. in')
c = 5 in [1, 2, 3, 4, 5]
print(c)
c = 1 not in [1, 2, 3, 4, 5]
print(c)
print()

print('10. list함수')
listD = [2, 5, 1, 3]
# 하나씩 추가
listD.append(4)
print(listD)
# 요소 많이 추가
listD.extend([1, 2, 3, 4, 5])
print(listD)

# 모든요소 삭제
listD.clear()
print(listD)
# 리스트 첫번째 특정 요소 제거
listDD = [1, 5, 23, 3, 5]
listDD.remove(3)
print(listDD)


# 리스트 카피 - 수정으로 원본이 바뀌는거 막음


def listChange(x):
    x[0] = 1000


listE = [1, 2, 3, 4, 5]
listChange(listE.copy())
print(listE)

# 리스트 안에 요소의 갯수 세기
listF = [1, 2, 3, 4, 2]
print(listF.count(1))

# 리스트 요소의 인덱스값 찾기, 제일 처음 인덱스만 나옴
print(listF.index(2))

# 리스트 해당되는 자리에 요소를 넣을 때
listF.insert(3, 1)
print(listF)

# 리스트 뒤에서 값을 꺼낼 때
listF.pop()
print(listF)
listF.pop(3)  # 인덱스
print(listF)

# 요소 뒤짚기
listF.reverse()
print(listF)
print()

print('11. 딕셔너리')
dic = {
    'one': '하나',
    'two': '둘',
    'three': '셋'
}
# 값 뽑기
print(dic.values())
# 키 뽑기
print(dic.keys())
# 리스트 안에 튜플로 뽑아내기 - zip
print(dic.items())

# 키 기준으로 제거
del dic['two']
print(dic)

# 데이터 넣기
dic['four'] = '넷'
print(dic)
print()

print('12. set')
# set 기본
s = set('11122345666')
print(s)
# 요소 추가
s.add(0)
print(s)
# 요소 많이 추가
s.update({11, 12, 13})
print(s)
# 삭제 - 삭제하려는 요소 안 넣으면 에러
s.discard(0)
print(s)
# 제거
s.remove('6')
print(s)
# 차집합 - difference
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7}
print(s1.difference(s2))
# 합집합 - union
print(s1.union(s2))
# 교집합 - intersection
print(s1.intersection(s2))
