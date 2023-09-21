#Função
#Calcule a media entre 2 valores a e b

def media(a,b):
    s = a + b
    m = s / 2 
    return m 

def mediapoderada(a, b, pa, pb):
    s = a*pa + b*pb 
    p= pa + pb 
    m = s / p
    return m 


print(f"o valor foi {media(6,9)}")

# implemente um programa em python,
# que recebe dois valores 
# e imprima a média entre eles, 
# defina uma função customizada
# para calcular a média.