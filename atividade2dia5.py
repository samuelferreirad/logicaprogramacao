horas=float(input("digite seu horario em brasilia: "))
def horasbb (horas):
    horas=horas%12
if (horas>=12):
    print("P.M" , horas,)
if (horas<=12):
    print("A.M",horas,)