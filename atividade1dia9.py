n1=0
n2=0
v1=0
v2=0
i=0
while(i<3):
    valor=float(input("digite um numero: "))
    if(valor>0) and (valor<=25):
        v1=v1+1
    if(valor>=26) and (valor<=50):
        n1=n1+1
    if(valor>=51) and (valor<=75):
        n2=n2+1
    if(valor>=76) and (valor<=100):
        v2=v2+1
    if(valor<0):
        i = 4
print("esses são os valores entre 0 e 20",v1)
print("esses são os valores entre 26",n1)
print("esses são os valores entre 51 e 75",n2)
print("esses são os valores entre 76 e 100",v2)
    

