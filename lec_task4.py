kol = int(input('Введите число: '))
kol += 1
a = 1
a2 = 0
for i in range(kol):
    print(a, end= ' ')
    a = a + a2
    a2 += 1
