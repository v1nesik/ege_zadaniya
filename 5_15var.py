for n in range(1000):
    a = bin(n)[2::]
    s = 0
    for i in range(len(a)):
        s = s+int(a[i])
    x = s % 2
    b = a + str(x)
    for i in range(len(b)):
        u = s+int(b[i])
    r = u % 2
    e = b + str(r)
    m = int(e, 2)
    if m > 55:
        print(m)
        break
