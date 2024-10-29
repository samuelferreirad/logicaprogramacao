soma1=0
soma2=0
for i in range(1,3):
    nome=float(input("digite seu nome: "))
    end=float(input("digite seu endereço: "))
    valor=float(input("digite o valor da compra: "))
    if(valor <=50.000):
        bonus=valor*1.10
        print(bonus)
    if(valor >50.000):
        bonus=valor*1.15
        print(bonus)