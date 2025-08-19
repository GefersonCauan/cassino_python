from datetime import datetime

def registrar_historico(jogo, aposta, resultado, saldo_final):
    with open("data/historico.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"[{timestamp}] Jogo: {jogo} | Aposta: {aposta} | Resultado: {resultado} | Saldo final: {saldo_final}\n")
