palavra_secreta = ["B", "A", "S", "I", "L", "I", "S", "C", "O"]
letras_descobertas = []

print("\n*** Jogo da Forca ***\n")

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False
tentativas_maximas = 6
tentativas = 0

def mostrar_forca(tentativas):
    boneco_forca = [
        "  ________",
        "  |     |",
        "  |     ",
        "  |     ",
        "  |     ",
        " _|_"
    ]
    if tentativas >= 1:
        boneco_forca[2] = "  |     O"
    if tentativas >= 2:
        boneco_forca[3] = "  |     |"
    if tentativas >= 3:
        boneco_forca[3] = "  |    /|"
    if tentativas >= 4:
        boneco_forca[3] = "  |    /|\\"
    if tentativas >= 5:
        boneco_forca[4] = "  |    /"
    if tentativas >= 6:
        boneco_forca[4] = "  |    / \\"

    for linha in boneco_forca:
        print(linha)

while not acertou and tentativas < tentativas_maximas:
    letra = input("Digite a letra: ").upper()

    if letra in palavra_secreta:
        print("Letra correta!")
        for i in range(len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                letras_descobertas[i] = letra
    else:
        print("Letra errada!")
        tentativas += 1

    print("Palavra: " + " ".join(letras_descobertas))
    mostrar_forca(tentativas)

    if "-" not in letras_descobertas:
        print("\nParabéns! Você acertou!")
        break

if "-" in letras_descobertas:
    print("\nVocê perdeu! A palavra era: " + "".join(palavra_secreta))
