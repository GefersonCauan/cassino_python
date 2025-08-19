
class Saldo:
    def __init__(self, valor_inicial=1000):
        self.valor = valor_inicial

    def apostar(self, quantia):
        if quantia > self.valor:
            print("⚠️ Saldo insuficiente!")
            return False
        self.valor -= quantia
        return True

    def adicionar(self, quantia):
        self.valor += quantia    