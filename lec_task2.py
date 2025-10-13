b1 = int(input('Первый член: '))
n = int(input('Кол-во: '))
q = int(input('знаменатель: '))
a = 1
n = n+1
while a !=n:
    ba = b1 * q**a-1
    a +=1
    print(ba)