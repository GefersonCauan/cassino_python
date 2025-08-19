import random
from utils import registrar_historico

# Números da roleta: cada número tem uma cor
NUMEROS = {
    0: "verde",
    1: "vermelho", 2: "preto", 3: "vermelho", 4: "preto", 5: "vermelho", 6: "preto",
    7: "vermelho", 8: "preto", 9: "vermelho", 10: "preto", 11: "preto", 12: "vermelho",
    13: "preto", 14: "vermelho", 15: "preto", 16: "vermelho", 17: "preto", 18: "vermelho",
    19: "vermelho", 20: "preto", 21: "vermelho", 22: "preto", 23: "vermelho", 24: "preto",
    25: "vermelho", 26: "preto", 27: "vermelho", 28: "preto", 29: "preto", 30: "vermelho",
    31: "preto", 32: "vermelho", 33: "preto", 34: "vermelho", 35: "preto", 36: "vermelho"
}

def jogar(saldo):
    print("\n=== 🎡 Roleta ===")
    print("1 - Apostar em número (0 a 36)")
    print("2 - Apostar em cor (vermelho/preto)")

    escolha = input("Escolha o tipo de aposta: ")

    try:
        aposta = int(input("Digite o valor da aposta: "))
    except ValueError:
        print("⚠️ Valor inválido.")
        return

    if not saldo.apostar(aposta):
        return

    numero_sorteado = random.randint(0, 36)
    cor_sorteada = NUMEROS[numero_sorteado]

    if escolha == "1":
        try:
            numero = int(input("Escolha um número de 0 a 36: "))
        except ValueError:
            print("⚠️ Número inválido. A aposta foi cancelada.")
            saldo.adicionar(aposta)  # devolve
            return

        if numero == numero_sorteado:
            ganho = aposta * 35
            print(f"🎉 Caiu {numero_sorteado} ({cor_sorteada})! Você GANHOU {ganho}!")
            saldo.adicionar(ganho)
            registrar_historico("Roleta", aposta, f"Ganhou {ganho}", saldo.valor)
        else:
            print(f"❌ Caiu {numero_sorteado} ({cor_sorteada}). Você perdeu!")
            registrar_historico("Roleta", aposta, "Perdeu", saldo.valor)

    elif escolha == "2":
        cor = input("Escolha uma cor (vermelho/preto): ").lower()
        if cor == cor_sorteada:
            ganho = aposta * 2
            print(f"🎉 Caiu {numero_sorteado} ({cor_sorteada})! Você GANHOU {ganho}!")
            saldo.adicionar(ganho)
            registrar_historico("Roleta", aposta, f"Ganhou {ganho}", saldo.valor)
        else:
            print(f"❌ Caiu {numero_sorteado} ({cor_sorteada}). Você perdeu!")
            registrar_historico("Roleta", aposta, "Perdeu", saldo.valor)

    else:
        print("⚠️ Opção inválida. A aposta foi cancelada.")
        saldo.adicionar(aposta)  # devolve o dinheiro
        registrar_historico("Roleta", aposta, "Aposta inválida (cancelada)", saldo.valor)
