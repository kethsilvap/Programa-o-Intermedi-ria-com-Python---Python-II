"""
Arquivo principal do jogo.
"""
import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import menu, imprimir_instrucoes, animacao_vitoria

def main():
    parser = argparse.ArgumentParser(description="Jogo Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--dificuldade", default=5, type=int)
    parser.add_argument("--color", default="white")
    parser.add_argument("--disable-sound", action="store_true")
    parser.add_argument("--modo", default="normal")

    args = parser.parse_args()

    print(f"Bem-vindo {args.name}!")

    while True:
        menu()
        op = input("Escolha: ")

        match op:
            case "1":
                lab = criar_labirinto(args.dificuldade)
                jogador = iniciar_jogador()

                while True:
                    imprimir_labirinto(lab)
                    cmd = input("Movimento (w/a/s/d): ")
                    jogador = mover(jogador, cmd, lab)
                    jogador = pontuar(jogador)

                    if jogador["x"] == len(lab)-1 and jogador["y"] == len(lab)-1:
                        print("Você venceu!")
                        animacao_vitoria(5)
                        break

            case "2":
                imprimir_instrucoes()

            case "3":
                print("Saindo...")
                break

            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()
