# 조건문
money = True

if money:
    print("택시 타기")
else:
    print("걸어가")

cash = 2000
card = 1
if 1 not in [1, 2, 3]:
    print("택시 타라")
else:
    print("걸어가")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass
elif card:
    print("택시타")
else:
    print("걸어가")

score = 70
message = "success" if score >= 60 else "fail"
print(message)


# 반복문
# while
treeHit = 0
while treeHit < 12:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

# for
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

b = 10
for i in range(2, b):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

c = [1, 2, 3, 4, 5]
result1 = [num*3 for num in c]
print(result1)

result2 = [num*2 for num in c if num % 2 == 0]
print(result2)
