"""
Interface de linha de comando para o pacote personalizador.
"""
import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    "1": layout,
    "layout": layout,
    "2": painel,
    "painel": painel,
    "3": progresso,
    "progresso": progresso,
    "4": estilo,
    "estilo": estilo
}

funcoes = {
    "layout": ["layout_duplo", "layout_vertical"],
    "painel": ["painel_simples", "painel_borda"],
    "progresso": ["progresso_simples", "progresso_lento"],
    "estilo": ["texto_colorido", "texto_alerta"]
}

def main():
    parser = argparse.ArgumentParser(description="Sistema de personalização com rich")
    parser.add_argument("texto", help="Texto ou caminho do arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica arquivo")
    parser.add_argument("-m", "--modulo", required=True, help="layout, painel, progresso, estilo")
    parser.add_argument("-f", "--funcao", required=True, help="nome ou índice da função")

    args = parser.parse_args()

    modulo = modulos.get(args.modulo)
    if not modulo:
        print("Módulo inválido")
        return

    nome_modulo = modulo.__name__.split('.')[-1]
    lista_funcoes = funcoes[nome_modulo]

    try:
        if args.funcao.isdigit():
            funcao_nome = lista_funcoes[int(args.funcao) - 1]
        else:
            funcao_nome = args.funcao
        funcao = getattr(modulo, funcao_nome)
    except:
        print("Função inválida")
        return

    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
