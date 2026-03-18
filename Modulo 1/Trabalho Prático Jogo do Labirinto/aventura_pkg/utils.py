"""
Funções utilitárias do jogo.
"""
import time

def imprimir_instrucoes():
    """Exibe instruções."""
    print("Use WASD para se mover até o E (saída).")

def menu():
    """Exibe menu."""
    print("1 - Jogar")
    print("2 - Instruções")
    print("3 - Sair")

def animacao_vitoria(n):
    """Função recursiva de animação."""
    if n == 0:
        return
    print("🎉 Vitória! 🎉")
    time.sleep(0.3)
    animacao_vitoria(n-1)
