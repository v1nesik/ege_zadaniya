# !В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 60 и хотя бы один из элементов кратен 15, затем максимальную из разностей элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17 (1).txt')
s = [int(i) for i in f]
cnt = 0
m = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if (abs(s[i] - s[j]) % 60 == 0) and ((s[i] % 15 == 0) or (s[j] % 15 == 0)):
            cnt += 1
            m = max(abs(s[i]-s[j]), m)
print(cnt, m)
