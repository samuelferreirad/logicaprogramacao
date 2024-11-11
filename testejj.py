#funções def
import random

def jogar_craps():
    resultado = random.randint(2, 12)
    print(f"Você tirou {resultado} na primeira jogada.")

    if resultado in [7, 11]:
        print("voce e natural: ")
    elif resultado in [2, 3, 12]:
        print("Você tirou craps")
    else:
        ponto = resultado
        print(f"Seu ponto é {ponto}. Tente tirar {ponto} novamente.")
        while True:
            resultado = random.randint(2, 12)
            print(f"Você tirou {resultado}.")
            if resultado == ponto :
                print("Você tirou o ponto novamente! Você ganhou")
                break
            elif resultado == 7:
                print("Você tirou 7 perdeu!")
                break

if __name__ == "__main__":
    jogar_craps()