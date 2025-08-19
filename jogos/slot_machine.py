import random
from utils import registrar_historico


def jogar(saldo):
    print("\n===  🎰 Slot Machine ===")
    aposta = int(input("Digite sua aposta: "))

    if not saldo.apostar(aposta):
        return
    
    simbolos = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
    resultado = [random.choice(simbolos) for _ in range(3)]

    print(" | ".join(resultado))

    if len(set(resultado)) == 1:
        ganho = aposta * 5
        print(f"🎉 JACKPOT! Você ganhou {ganho}!")
        saldo.adicionar(ganho)
        registrar_historico("Slot Machine", aposta, f"Ganhou {ganho}", saldo.valor)
    elif len(set(resultado)) == 2:
        ganho = aposta * 2
        print(f"✨ Dois iguais! Você ganhou {ganho}!")
        saldo.adicionar(ganho)
        registrar_historico("Slot Machine", aposta, f"Ganhou {ganho}", saldo.valor)
    else:
        print("💔 Você perdeu!")
        registrar_historico("Slot Machine", aposta, "Perdeu", saldo.valor)
  