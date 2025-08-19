import random
from utils import registrar_historico


# Baralho (sem naipes, só valores)
CARTAS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def valor_carta(carta):
    if carta in ["J", "Q", "K"]:
        return 10
    elif carta == "A":
        return 11  # Ás começa valendo 11, ajustamos depois
    else:
        return int(carta)

def calcular_pontos(mao):
    total = sum(valor_carta(c) for c in mao)
    # Ajuste do Ás (pode valer 1 ou 11)
    ases = mao.count("A")
    while total > 21 and ases:
        total -= 10  # transforma Ás de 11 -> 1
        ases -= 1
    return total

def mostrar_mao(jogador, mao, esconder_primeira=False):
    if esconder_primeira:
        print(f"{jogador}: [?, {mao[1]}]")
    else:
        print(f"{jogador}: {mao} (total = {calcular_pontos(mao)})")

def jogar(saldo):
    print("\n=== ♠️♥️ Blackjack ===")
    aposta = int(input("Digite o valor da aposta: "))
    if not saldo.apostar(aposta):
        return

    # Distribuir cartas
    baralho = CARTAS * 4  # 4 naipes
    random.shuffle(baralho)

    jogador = [baralho.pop(), baralho.pop()]
    dealer = [baralho.pop(), baralho.pop()]

    # Mostrar mãos
    mostrar_mao("Jogador", jogador)
    mostrar_mao("Dealer", dealer, esconder_primeira=True)

    # Turno do jogador
    while calcular_pontos(jogador) < 21:
        acao = input("Você quer (H)it ou (S)tand? ").lower()
        if acao == "h":
            jogador.append(baralho.pop())
            mostrar_mao("Jogador", jogador)
            if calcular_pontos(jogador) > 21:
                print("💥 Você estourou! Perdeu a aposta.")
                return
        elif acao == "s":
            break
        else:
            print("⚠️ Opção inválida. Digite H ou S.")

    # Turno do dealer
    mostrar_mao("Dealer", dealer)
    while calcular_pontos(dealer) < 17:
        dealer.append(baralho.pop())
        mostrar_mao("Dealer", dealer)

    pontos_jogador = calcular_pontos(jogador)
    pontos_dealer = calcular_pontos(dealer)

    # Resultado
    if pontos_dealer > 21 or pontos_jogador > pontos_dealer:
        ganho = aposta * 2
        print(f"🎉 Você ganhou! +{ganho}")
        saldo.adicionar(ganho)
        registrar_historico("Blackjack", aposta, f"Ganhou {ganho}", saldo.valor)
    elif pontos_jogador == pontos_dealer:
        print("🤝 Empate! A aposta foi devolvida.")
        saldo.adicionar(aposta)
        registrar_historico("Blackjack", aposta, "Empate", saldo.valor)
    else:
        print("💔 O dealer ganhou. Você perdeu.")
        registrar_historico("Blackjack", aposta, "Perdeu", saldo.valor)
