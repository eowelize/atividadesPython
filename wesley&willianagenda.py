#essa é uma agenda
#   Criar contato


def criar_contato():
    nome=input("Digite o nome do contato:")
    endereço=input("Selecione o endereço do contato:")
    número=int(input("Digite o número do Contato:"))
    categoria=input("Digite o tipo do contato: Pessoal,Profissional ou Romantico:")

    with open("agenda de contato.txt", "a") as arquivo:
        arquivo.write(f"{nome},{endereço},{número},{categoria}\n")
    print("Seu contato foi adicionado com sucesso!")

# exibir os contatos

def listar_contato():
    with open("agenda de contato.txt", "r") as arquivo:
        for linha in arquivo:
            nome, endereco, telefone, categoria = linha.strip().split(",")
            print(f"Nome: {nome}, Endereço: {endereco}, Telefone: {telefone}, Categoria: {categoria}")
#editar os contatos
def editar_contato():
    nome_alvo = input("Digite o nome do contato que deseja editar: ")
    with open("agenda de contato.txt", "r") as arquivo:
        contatos = arquivo.readlines()

    
    contatos_editados = []

    
    for contato in contatos:
        nome, endereco, telefone, categoria = contato.strip().split(",")

        
        if nome == nome_alvo:
            endereco = input("Digite o novo endereço: ")
            telefone = input("Digite o novo numero: ")
            categoria = input("Digite a nova categoria (pessoal, profissional, romantico): ")
            contato = f"{nome},{endereco},{telefone},{categoria}\n"

        contatos_editados.append(contato)

   
    with open("agenda de contato.txt", "w") as arquivo:
        arquivo.writelines(contatos_editados)

    print("Contato editado com sucesso!")
#   excluir um contato
def excluir_contato():
    nome_alvo = input("Digite o nome do contato que deseja excluir: ")
    with open("agenda de contato.txt", "r") as arquivo:
        contatos = arquivo.readlines()
    contatos_nao_excluidos = []
    for contato in contatos:
        nome, _, _, _ = contato.strip().split(",")
        if nome != nome_alvo:
            contatos_nao_excluidos.append(contato)
    with open("agenda de contato.txt", "w") as arquivo:
        arquivo.writelines(contatos_nao_excluidos)

    print("Contato excluído com sucesso!")

#Salvar agenda 
def salvar_agenda(contatos):
    with open("agenda_de_contato.txt", "w") as arquivo:
        for contato in contatos:
            arquivo.write(f"Nome: {contato['nome']}\n")
            arquivo.write(f"Telefone: {contato['endereço']}\n")
            arquivo.write(f"Email: {contato['numero']}\n")
            arquivo.write(f"Email: {contato['categoria']}\n")
            arquivo.write("\n")
#Escolher a categoria
def main():
    while True:
        print("\n*** Agenda de Contatos ***")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_contato()
        elif opcao == "2":
            listar_contato()
        elif opcao == "3":
            editar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
