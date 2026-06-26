#Rafael Henrique Woss, R.A: 10771377 
import random

# Gabarito dos atributos
gabarito = ["Nome", "Velocidade", "Tanque", "Ano"]

# Baralho
baralho_original = [
    ["Toyota Yaris Cross", 175, 36, 2024],
    ["Ferrari F40", 324, 120, 1987],
    ["Lamborghini Aventador", 350, 90, 2011],
    ["Bugatti Chiron", 420, 100, 2016],
    ["Porsche 911", 310, 64, 2023],
    ["McLaren P1", 350, 72, 2013],
    ["Audi R8", 330, 83, 2021],
    ["BYD Song Plus", 170, 60, 2023]
]



# FUNÇÕES

def embaralhar_e_distribuir():
    baralho = baralho_original[:]

    random.shuffle(baralho)

    mao_jogador1 = []
    mao_jogador2 = []

    for i in range(len(baralho)):

        if i % 2 == 0:
            mao_jogador1.append(baralho[i])

        else:
            mao_jogador2.append(baralho[i])

    return mao_jogador1, mao_jogador2


def mostrar_carta(carta):

    print("\nCarta atual:")

    for i in range(len(gabarito)):
        print(f"{i} - {gabarito[i]}: {carta[i]}")


def escolher_atributo():

    atributo = int(input("\nEscolha o atributo: "))

    while atributo < 1 or atributo > 3:
        atributo = int(input("Digite um valor entre 1 e 3: "))

    return atributo


def jogar_partida(single_player):

    mao1, mao2 = embaralhar_e_distribuir()

    monte_espera = []

    rodada = 1

    while len(mao1) > 0 and len(mao2) > 0:

        print("\n========================")
        print(f"RODADA {rodada}")
        print("========================")

        carta1 = mao1[0]
        carta2 = mao2[0]

        print("\nJogador 1")
        mostrar_carta(carta1)

        # SINGLE PLAYER
        if single_player:

            atributo = escolher_atributo()

        # MULTIPLAYER
        else:

            atributo = escolher_atributo()

        print("\nCarta do adversário:")
        mostrar_carta(carta2)

        valor1 = carta1[atributo]
        valor2 = carta2[atributo]

        print(f"\nJogador 1 -> {valor1}")
        print(f"Jogador 2 -> {valor2}")

        # Remove as cartas do topo
        carta_j1 = mao1.pop(0)
        carta_j2 = mao2.pop(0)

        # Jogador 1 vence
        if valor1 > valor2:

            print("\nJogador 1 venceu a rodada!")

            mao1.append(carta_j1)
            mao1.append(carta_j2)

            # Entrega monte acumulado
            for carta in monte_espera:
                mao1.append(carta)

            monte_espera = []

        # Jogador 2 vence
        elif valor2 > valor1:

            print("\nJogador 2 venceu a rodada!")

            mao2.append(carta_j2)
            mao2.append(carta_j1)

            # Entrega monte acumulado
            for carta in monte_espera:
                mao2.append(carta)

            monte_espera = []

        # Empate
        else:

            print("\nEmpate!")
            print("Cartas foram para o monte de espera.")

            monte_espera.append(carta_j1)
            monte_espera.append(carta_j2)

        print(f"\nCartas Jogador 1: {len(mao1)}")
        print(f"Cartas Jogador 2: {len(mao2)}")
        print(f"Monte de espera: {len(monte_espera)}")

        rodada += 1

    # Resultado final
    print("\n========================")
    print("FIM DE JOGO")
    print("========================")

    if len(mao1) > 0:
        print("\nJogador 1 é o vencedor!")

    else:
        print("\nJogador 2 é o vencedor!")


# MENU PRINCIPAL


while True:

    print("\n========================")
    print("SUPER TRUNFO")
    print("========================")
    print("1 - Single Player")
    print("2 - Multiplayer")
    print("3 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:

        jogar_partida(True)

    elif opcao == 2:

        jogar_partida(False)

    elif opcao == 3:

        print("\nEncerrando o jogo...")
        break

    else:

        print("\nOpção inválida!")