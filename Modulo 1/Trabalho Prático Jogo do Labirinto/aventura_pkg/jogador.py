"""
Módulo responsável pelo jogador.
"""

def iniciar_jogador():
    """Inicializa posição e pontuação."""
    return {"x": 0, "y": 0, "pontos": 0}

def mover(jogador, comando, lab):
    """Move o jogador baseado em comando WASD."""
    x, y = jogador["x"], jogador["y"]

    match comando:
        case "w":
            x -= 1
        case "s":
            x += 1
        case "a":
            y -= 1
        case "d":
            y += 1

    if 0 <= x < len(lab) and 0 <= y < len(lab):
        if lab[x][y] != "#":
            jogador["x"], jogador["y"] = x, y

    return jogador

def pontuar(jogador):
    """Incrementa pontuação."""
    jogador["pontos"] += 1
    return jogador
