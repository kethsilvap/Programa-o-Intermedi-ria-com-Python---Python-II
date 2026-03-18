"""
Módulo responsável pela criação e exibição do labirinto.
"""
import random

def criar_labirinto(tamanho=5):
    """Cria um labirinto simples aleatório."""
    lab = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    for _ in range(tamanho):
        x, y = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
        lab[x][y] = "#"
    lab[0][0] = "P"
    lab[tamanho-1][tamanho-1] = "E"
    return lab

def imprimir_labirinto(lab):
    """Imprime o labirinto no terminal."""
    for linha in lab:
        print(" ".join(linha))
