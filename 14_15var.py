a = 49**6 + 7**19 - 21
b = ''
while a > 0:
    b = b + str(a % 7)
    a = a//7
print(b.count('0'))
