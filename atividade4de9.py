#atividade 4 de 9:
d=0
f=0
for i in range(5):
    v=float(input("digite um umero: "))
    if 10 <= v <=20:
       d+=1
    else:
       f+=1
print(f"numeros dentros (10 20) {d}")
print(f"numeros fora de (10 20) {f}")