# 4, 5, 6, 8, 9 ou 10

import random
numero1=0
numero2=100
for i  in range(2):
    numero1=random.randint(2, 12)
    print(numero1)
if numero1 == 7 or numero1 == 11:
    print("você e um natural ")
if numero1 == 2 or numero1==3 or numero1==12:
    print("craps")
if numero2 == 4 or numero2 == 5 or numero2 ==  6 or numero2 == 9 or numero2  == 8 or numero2 == 10:
    print("ponto")
if numero1 == numero2:
    print("você ganhou ")
