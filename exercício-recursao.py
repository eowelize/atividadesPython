import time
def contagemRegressiva(i:int):
    if(i <= 0): print(0)
    else:
        time.sleep(1)
        print(i)
        contagemRegressiva(i-1)
    
def somaRecursiva(i: int):
    if(i <= 1): return 1 
    return somaRecursiva(i-1)

#Exercício 1: Pontência Recursiva
def potencia(base, expoente):
    if expoente == 0: return 1 
    else: return base * potencia(base, expoente - 1)
print(potencia(2, 3))

s = ""

#Exercício 3: Inversão de String
def inverter_string(s):
    if len(s) == 0: return ""
    else: return s[-1] + inverter_string(s[:-1])

    print("inverter strings")
    print(f'recursividade : {inverter_string("recursividade")}')
    print(f'inconstitucionalissimamente : {inverter_string("inconstitucionalissimamente")}')
    print(f'paralelepipedo : {inverter_string("paralelepipedo")}')
    