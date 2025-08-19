from saldo import Saldo
from jogos import slot_machine, roleta, blackjack

def manu():
    print("\n===🎰 Cassino Python ===")
    print("1 - Slot Machine (caça-niquel)")
    print("2 - Roleta")
    print("3 - Blackjack")
    print("4 - Sair")


def main():
    saldo = Saldo(1000)
    while True:
        print(f"\💰 Seu saldo: {saldo.valor}")
        manu()
        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            slot_machine.jogar(saldo)
        elif opcao == "2":
            roleta.jogar(saldo)
        elif opcao == "3":
            blackjack.jogar(saldo)
        elif opcao == "4":
            print("\nObrigado por jogar! 👋")
            break
        else:
            print("\n⚠️ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()                            