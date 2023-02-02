# 입력
a = input("숫자를 입력하세요 >>")
print(a)

# print
print("a" "b" "c" "dss")
print("a", "b", "c", "dss")

for i in range(10):
    print(i, end=';')
print('')

# 파일 읽기
f = open("newFile.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 쓰기
g = open("newFile.txt", 'r', encoding="UTF-8")
line = g.readline()
print(line)
g.close()

# 한줄 읽기
h = open("newFile.txt", 'r', encoding="UTF-8")
while True:
    line = h.readline()
    if not line:
        break
    print(line)
h.close

# 리스트로 읽기
i = open("newFile.txt", 'r', encoding="UTF-8")
lines = i.readlines()
for line in lines:
    print(line.strip("\n"))
i.close()

# 통채로 읽기
j = open("newFile.txt", 'r', encoding="UTF-8")
data = j.read()
print(data)
f.close()

# 추가 입력
k = open("newFile.txt", 'a', encoding="UTF-8")
for i in range(11, 20):
    data = "%d번쨰 줄입니다.\n" % i
    k.write(data)
k.close()

# close 안하는 방법
with open("foo.txt", 'w') as l:
    l.write("Life is too short")
