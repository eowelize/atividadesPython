x = float(input("Escreva um numero"))
y = float(input("Escreva outro numero"))

import math

print(f"Essas são suas codernadas x e y respectivamente: {x} e {y}")

terceiro = float(input("Insira um valor para representar uma força em newtons"))
quarto = float(input("Insira mais um valor para representar uma força em newtons"))

import math 

AnguloEmGrau = quarto

força = terceiro #newtons 
angulo_graus = quarto #ângulo
m = 0.5 #peso da bala

teta = angulo_graus
rteta = math.radians(teta)
sen_teta = math.sin(teta)
cos_teta = math.cos(rteta)
g = float(10)

print(rteta)
print(sen_teta)
print(cos_teta)

#calculo 1: a velocidade inicial do lançamento obliquio

def velocidadeinicialx (velocidadeinicial, cos_teta): #x é a velocidade horizontal
    j = velocidadeinicial * cos_teta
    return j

def velocidadeinicialy (velocidadeinicial, sen_teta):
    w = velocidadeinicial * sen_teta
    return w

def velocidadeinicial (força, m):
    e = força * 1/m
    return e

def velocidadey (velocidadeinicialy, g, t):
    z = velocidadeinicial - g * t
    return z

def velocidadex (velocidadeinicialx):
    k = velocidadeinicialx
    return k

def tempomax (velocidadeinicialy, g):
    q = 2 * velocidadeinicialy/g
    return q

def verticalmax (x, velocidadeinicialx, tempomax):
    c = x + velocidadeinicialx * tempomax
    return c

def verticalmax (x, velocidadeinicialx, tempomax):
    k = x + velocidadeinicialx * tempomax
    return k

def horizontalmax (y, velocidadeinicialy, tempo, g, tempomax):
    tempo = tempomax / 2
    l = y + velocidadeinicialy*tempo - g*tempo**2/2
    return l

#VELOCIDADE VERTICAL E HORIZONTAL EM CADA INSTANTE DO VOO

finalizar2 = False
finalizar = False

while(not finalizar2):
    o = input("Digite y para colocar um tempo específico para o tamanho da lista (lembre que o limite é o tempo máximo)")
    if o == "y":
        finalizar2 = True
        while(not finalizar):
            t = float(input("Digite aqui o tempo que você quer (lembre que o limite é o tempo máximo): "))
            if t < tempomax():
                finalizar = True
           
                def veloy1(t):
                    g_local = -g
                    haha = g_local * t
                    veloy22 = velocidadeinicialy() + haha
                    return veloy22
            print(f"A velocidade y nesse tempo é: {veloy1(t):.4f}")
        else:
            print("Escreva um número menor do que o tempo máximo.")




print(f"A velocidade horizontal é {velocidadeinicialx():.3f}")

def dist():
    my = max() - cordx
    return my 

print(f"A distância entre o ponto de lançamento e local da queda: {dist():.3f}")

import time 
import math
g = float(10)

velocidades_y = []

#LOOP QUE CALULA AS VELOCIDADES EM CASA INSTANTE O VOO

for t in range(int(tempomax()) + 1):
    vel_y = veloy1(t)
    velocidades_y.append(vel_y)

#IMPRIME AS VELOCIDADES DE Y EM CADA INSTANTE DO VOO

print("Velocidades de y em cada instante do voo:")
for t, vel_y in enumerate(velocidades_y):
    print(f"Tempo {t}: Velocidade y = {vel_y:.4f}")

print(f"a distancia alcançada foi de: {max():.3f}")