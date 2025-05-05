palavra_secreta = ["F", "A", "Z", "O", "L",]

desenhos_forca = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

tentativas_erradas = 1
nivel_forca = 0
mensagem_final = "Você Perdeu!!"
entrada_usuario = input("Digite uma letra: ").upper()
letras_digitadas = []
letras_descobertas = ["_"] * len(palavra_secreta)

while tentativas_erradas < 6:

    letras_digitadas.append(entrada_usuario)
    print(f"\nLetras já digitadas: {letras_digitadas}\n")

    if entrada_usuario in palavra_secreta:
        for indice in range(len(palavra_secreta)):
            if palavra_secreta[indice] == entrada_usuario:
                letras_descobertas[indice] = entrada_usuario

        print(f"Letras corretas até agora: {letras_descobertas}")
        print("Acertou!")
        print(desenhos_forca[nivel_forca])

        if letras_descobertas == palavra_secreta:
            mensagem_final = "Você venceu!!"
            break

        entrada_usuario = input("Digite uma letra: ").upper()

    else:
        nivel_forca += 1
        print(f"Letras corretas até agora: {letras_descobertas}")
        print(desenhos_forca[nivel_forca])
        entrada_usuario = input("Digite uma letra: ").upper()
        tentativas_erradas += 1

if mensagem_final != "Você venceu!! FAZ O L":
    nivel_forca += 1

print(desenhos_forca[nivel_forca])
print(mensagem_final)
