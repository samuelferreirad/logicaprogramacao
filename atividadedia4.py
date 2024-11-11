ca = 5
m = 5
t = 5
c = 5
ba = 5
soma = 0
total = 0 
totalp = 0
pequena = 20
media = 30
grande = 40
totalv = 0

contador_pedidos = 0  
maior_pedido = 0  

while True:  
    pd = str(input("Digite o tamanho da pizza (pequena, media, grande): "))
    if pd == 'pequena':
        totalp += pequena
        print('Pequena: 20 reais')
    elif pd == 'grande':
        totalp += grande
        print("Grande: 40 reais")
    elif pd == 'media':
        totalp += media
        print("Média: 30 reais")
    else:
        print("Tamanho inválido. Tente novamente.")
        continue  

    ingredientes = ['cebola', 'mussarela', 'tomate', 'calabresa', 'bacon']
    for ingrediente in ingredientes:
        pedido = str(input(f"Deseja {ingrediente}? (sim/não): "))
        if pedido == 'sim':
            soma += 5
            total += 5
    
    totalv = total + totalp
    print(f"Total do pedido: {totalv} reais")

    contador_pedidos += 1
    if totalv > maior_pedido:
        maior_pedido = totalv

    n1 = str(input("Deseja fazer um novo pedido? (sim/não): "))
    if n1.lower() != 'sim':
        break  

    totalp = 0
    total = 0
    soma = 0

print(f"Total de pedidos realizados: {contador_pedidos}")
print(f"Maior pedido foi de: {maior_pedido} reais")