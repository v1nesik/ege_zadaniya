# !В файле содержится последовательность из 10 000 натуральных чисел. Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, у которых различные остатки от деления на d  =  160 и хотя бы одно из чисел делится на p  =  7, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17 (2).txt')
s = [int(i) for i in f]
count = 0
m = 0
for i in range(len(s)-1):
    for j in range(i + 1, len(s)):
        if (s[i] % 160 != s[j] % 160) and (s[i] % 7 == 0 or s[j] % 7 == 0):
            count += 1
            m = max(s[i]+s[j], m)
print(count, m)
