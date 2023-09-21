
print("-----------------------------------------------------------------------------")

a = "medo"
b = "Givanio"
c = "MMA"
d = "do seu treino de peso na academia"
e = "seu pai"
f = "o jegue que te cagou"
g = "Bolsonaro"
h = "CR7"
i = "Kung Fu Panda"
j = "Sim"

print("--------------------------------------------------------------------")

resposta_usuario_1 = input("no 2°B não existe o que?")
resposta_usuario_2 = input("qual o melhor professor do senai?")
resposta_usuario_3 = input("Qual o melhor esporte?")
resposta_usuario_4 = input("de onde o namorado de thaís carla tira força pra aguentar ela??")
resposta_usuario_5 = input("quem veio primeiro o ovo ou a galinha?")
resposta_usuario_6 = input("Quem te perguntou?")
resposta_usuario_7 = input("Quem foi o melhor presidente, Lula ou Bolsonaro?")
resposta_usuario_8 = input("Quem é o melhor, CR7 ou Anão?")
resposta_usuario_9= input("Qual é a melhor triologia, Kung Fu Panda ou Como treinar seu Dragão?")
resposta_usuario_10 = input("Eu sou o coringa?")

print("------------------------------------------------------------------------------------")

nota = 0

if (resposta_usuario_1 == a): print("Parabéns, você pensa muito!!!"); nota = nota + 1
if (resposta_usuario_2 == b): print("Parabéns, você pensa pouco!!!"); nota = nota + 1
if (resposta_usuario_3 == c): print("Parabéns, você pensa muito!!!"); nota = nota + 1
if (resposta_usuario_4 == d): print("Parabéns, você pensa pouco!!!"); nota = nota + 1
if (resposta_usuario_5 == e): print("Parabéns, você pensa muito!!!"); nota = nota + 1
if (resposta_usuario_6 == f): print("Parabéns, você pensa muito!!!"); nota = nota + 1
if (resposta_usuario_7 == g): print("Parabéns, você pensa pouco!!!"); nota = nota + 1
if (resposta_usuario_8 == h): print("Parabéns, você pensa muito!!!"); nota = nota + 1
if (resposta_usuario_9 == i): print("Parabéns, você pensa pouco!!!"); nota = nota + 1
if (resposta_usuario_10 == j): print("Parabéns, você pensa muito!!!"); nota = nota + 1

if(nota == 0):
    print("Parabéns!! você não acertou nenhuma questão...")

else:
    print(f"suanota foi: {nota}")

    input("PRESSIONE ENTER PARA CONTINUAR...")