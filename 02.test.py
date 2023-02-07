from collections import Counter
n = 10

result = range(1, n, 2)
print(list(result))


def solution(array, n):
    answer = Counter(array).get(n)
    if answer == None:
        return 0

    return answer
