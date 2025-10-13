a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <=a:
    print('Такого треугольника не существует')
else:
    if a == b or a == c or b == c:
        print('Равнобедрянный')
    elif a == b and a == c and b == c:
        print('Равностороний') 
    else:
        print('разносторонний')  