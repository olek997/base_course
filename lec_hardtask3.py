chislo = int(input())
a1 = chislo%10
a10 = (chislo//10)%10
a100 = (chislo//100)%10
a1000 = chislo//1000
print(f'{a1}{a10}{a100}{a1000}')