#faça um programa que receba a idade, altura eo peso de 25 pessoas e mostre a quantidade de pessoas com idade superior a 50 anos 
f=0
i=0
while(i<3):
    i+=1
    idade=int(input("digite sua idade: "))
    altura=int(input("digite seu altura: "))
    peso=int(input("digite seu peso: "))
    if(idade>50):
        f+=1
print(f," pessoas ")