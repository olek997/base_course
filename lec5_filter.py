numbers = [16, 25, 19, 41]

def isEven(a):
    return (a % 2 == 0)
print(list(filter(isEven, numbers)))