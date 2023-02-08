# 1강

import re
import numpy as np

numbers = [1, 2, 3, 4, 5]
print(numbers)
newNum = np.array(numbers)
print(newNum)
print((newNum*2).tolist())
print(list(newNum*2))


def solution(numbers):
    return list(map(lambda x: x*2, numbers))


# def doubling(x):
#     retrurn x*2


def solution(numbers):
    return list(map(doubling, numbers))


# 2강 -문자열 뒤집기


result1 = re.sub('[1-9]', '', 'B123ddj3d8AAwhf922FEGEDf32PP')
result2 = re.sub('[a-z]', '', 'B123ddj3d8AAwhf922FEGEDf32PP')
result3 = re.sub('[A-Z]', '', 'B123ddj3d8AAwhf922FEGEDf32PP')
result4 = re.sub('[a-zA-Z]', '', 'B123ddj3d8AAwhf922FEGEDf32PP')
print(result1)
print(result2)
print(result3)
print(result4)
