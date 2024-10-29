maior=0
menor=10000
cmenos=None
cmais=0
for i in range(2):
    numero=int(input("digite seu numero "))
    altura=float(input("digit sua alturara: "))
    if altura > maior:
        maior=altura
        cmais=numero
    if altura < menor:
        menor=altura
        cmenos=numero
print(f"alunos mais alto ",{maior},{cmais})
print(f"alunos mais baixo ",{menor},{cmenos})
