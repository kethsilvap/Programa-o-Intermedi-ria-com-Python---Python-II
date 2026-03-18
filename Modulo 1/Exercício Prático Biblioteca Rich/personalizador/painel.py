"""
Módulo responsável por funcionalidades de painel usando rich.
"""
from rich.console import Console
from rich.panel import Panel

console = Console()

def ler_conteudo(texto, isArquivo):
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            return f.read()
    return texto

def painel_simples(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    console.print(Panel(conteudo, title="Painel Simples"))

def painel_borda(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    console.print(Panel(conteudo, border_style="red", title="Destaque"))
