dic = {'name':'kim', 'age':37}
a = {1:111, 2:222, 3:333}

# 출력
print(dic['name'])

# 추가
dic['address'] = 'hanam'
print(dic)

# 삭제
del dic['address']
print(dic)
# 모두 삭제
print(a)
a.clear()
print(a)

# 키 뽑기
print(dic.keys())
# 키 있나 확인 - boolean
print('name' in dic)
print(37 in dic)

# 값 뽑기
print(dic.values())
# 특정값 뽑기 - get은 값 없을 때 에러 안남 None으로 표시
print(dic.get('name'))

# 아이템화
print(dic.items())


