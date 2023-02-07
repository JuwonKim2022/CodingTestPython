from collections import Counter

array = [1, 2, 3, 4, 5, 11, 111]
arrayStr = str(array)

answer = Counter(arrayStr).get('1')

print(answer)
