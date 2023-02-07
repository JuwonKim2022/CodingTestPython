array = [1, 1, 2, 3, 4, 11]

print(str(array))
print(str(array).count('1'))

age = 23
p = 'abcdefghij'
print(''.join(list(map(lambda x: p[int(x)], str(age)))))
print(list(map(lambda x: p[int(x)], str(age))))
print(map(lambda x: p[int(x)], str(age)))
print(lambda x: p[int(x)], str(age))
