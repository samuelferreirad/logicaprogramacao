#aividade 2
impar=0
par=0
for i in range(10):
    va=int(input("digite um numero: "))
    if(va%2==0):
      print("esse valor é par")
    par=par+1
else:
      print("esse numero e impar")
print(par)
print(impar)