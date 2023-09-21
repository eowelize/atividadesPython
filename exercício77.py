alunos = []
notas = []

concluir = False

while (not concluir):
    print("Digite o nome do aluno:")
    nomeAluno = input()
    print("Digite a nota do aluno")
    notaAluno = int(input())

    if(notaAluno < 5): print("Misericórdia")
    elif(notaAluno < 7): print("Tá quase")
    else: print("Passsssssou")

    alunos.append(nomeAluno)
    notas.append(notaAluno)

    print("Deseja inserir outra nota?(s/n)")
    concluir = input() == "n"

print("Seguem abaixo todas as notas digitadas:")
print("Aluno : Nota")
filename = "meuArquivo"
for i in range(len(alunos)):
    print(f"{alunos[i]} : {notas[i]}")

input("Pressione Enter pra terminar...")
