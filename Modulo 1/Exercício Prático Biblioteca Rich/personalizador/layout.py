"""
Módulo responsável por funcionalidades de layout usando rich.
"""
from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel

console = Console()

def ler_conteudo(texto, isArquivo):
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            return f.read()
    return texto

def layout_duplo(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    layout = Layout()
    layout.split_row(
        Layout(Panel(conteudo[:len(conteudo)//2], title="Parte 1")),
        Layout(Panel(conteudo[len(conteudo)//2:], title="Parte 2"))
    )
    console.print(layout)

def layout_vertical(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    layout = Layout()
    layout.split_column(
        Layout(Panel(conteudo, title="Topo")),
        Layout(Panel("Rodapé", title="Base"))
    )
    console.print(layout)
