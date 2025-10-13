a = int(input())
b = int(input())
c = a%b
if b!=0 and c==0:
    print('Делится нацело. Частное: ', a//b)
elif b!=0 and c>0:
    print('Число не делится нацело. Частное: ', a//b, 'Остаток: ',c)    