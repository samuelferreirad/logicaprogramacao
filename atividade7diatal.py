#atividade 5
n=int(input("digite um numero: "))
if n>1:
   for i in range(2,n):
    if n%i==0:
        print("não é numero primo ")
        break
    else:
        print("e um numero primo: ")
else:  
    print("kkkkk")
