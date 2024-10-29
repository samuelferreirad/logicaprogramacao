gabarito=("a","b","c","d","e","e","d","c","b","a")
acertos=0
erros=0
soma=0
while True:
    nota1=(input("digite a responta da questão 1 :"))
    nota2=(input("digite a responta da questão 2 :"))
    nota3=(input("digite a responta da questão 3 :"))
    nota4=(input("digite a responta da questão 4 :"))
    nota5=(input("digite a responta da questão 5 :"))
    nota6=(input("digite a responta da questão 6 :"))
    nota7=(input("digite a responta da questão 7 :"))
    nota8=(input("digite a responta da questão 8 :"))
    nota9=(input("digite a responta da questão 9 :"))
    nota10=(input("digite a resposta da questão 10: "))
    if nota1=='a':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota2=='b':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota3=='c':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota4=='d':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota5=='e':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota6=='e':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota7=='d':
        acertos+=1
        soma+=1
    else:
        erros=+1
    if nota8=='c':
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota9=="b":
        acertos+=1
        soma+=1
    else:
        erros+=1
    if nota10=="a":
        acertos+=1
        soma+=11
    else:
        erros+=1
    print("seu total de acertos",acertos)
    print("seu total de erros",erros)
    print("soma total ",soma)
    for denovo in range (1):
        denovo=input("quer continua: ")
    if denovo =='não':
            break