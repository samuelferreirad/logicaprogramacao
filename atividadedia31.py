ca=5
m=5
t=5
c=5
ba=5
soma=0
total=0 
totalp=0
pequena=20
media=30
grande=40
totalp=0
totalv=0
for i in range(1):
    pd=str(input("digite to tamanho da pizza: "))
    if pd=='pequena':
        totalp+=20
        print('pequena 20 reais ')
    if pd=='grande':
        totalp+=40
        print("grande 40 reais ")
    if pd=='media':
        totalp+=30
        print("media 30 reais")
    pedido1=str(input("deseja cebola: "))
    if pedido1=='sim':
        soma+=5
        total+=5
        if pedido1=='nao':
            break
    pedido2=str(input("deseja mussarela: "))
    if pedido2=='sim':
        soma+=5
        total+=5
        if pedido2=='nao':
            break
    pedido3=str(input("deseja tomate: "))
    if pedido3=='sim':
        soma+=5
        total+=5
    if pedido3=='nao':
        break
    pedido4=str(input("deseja calabresa: "))
    if pedido4=='sim':
        soma+=5
        total+=5
        if pedido4=='nao':
            break
    pedido5=str(input("deseja bacon: "))
    if pedido5=='sim':
        soma+=5
        total+=5
    if pedido5=='nao':
        break
    totalv=total+totalp
print(totalv)
print("O PEDIDO IRA CHEGAR EM 45 MINUTOS: ")

n1=str(input("deseja fazer um novo pedido: "))
if n1 =='sim':
 for i in range(1):
    pd=str(input("digite to tamanho da pizza: "))
    if pd=='pequena':
        totalp+=20
        print('pequena 20 reais ')
    if pd=='grande':
        totalp+=40
        print("grande 40 reais ")
    if pd=='media':
        totalp+=30
        print("media 30 reais")
    pedido1=str(input("deseja cebola: "))
    if pedido1=='sim':
        soma+=5
        total+=5
        if pedido1=='nao':
          break
    pedido2=str(input("deseja mussarela: "))
    if pedido2=='sim':
        soma+=5
        total+=5
        if pedido2=='nao':
            break  
    pedido3=str(input("deseja tomate: "))
    if pedido3=='s  im':
        soma+=5  
        total+=5  
    if pedido3=='n  ao':
        break
    pedido4=str(input("deseja calabresa: "))
    if pedido4=='sim':
        soma+=5
        total+=5
        if pedido4=='nao':
            break
    pedido5=str(input("deseja bacon: "))
    if pedido5=='sim':
        soma+=5
        total+=5
    if pedido5=='nao':
        break
    totalv=total+totalp

            
