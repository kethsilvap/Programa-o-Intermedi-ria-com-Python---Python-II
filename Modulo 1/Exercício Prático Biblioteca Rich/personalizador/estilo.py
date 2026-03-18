"""
Módulo responsável por funcionalidades de estilo usando rich.
"""
from rich.console import Console

console = Console()

def ler_conteudo(texto, isArquivo):
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            return f.read()
    return texto

def texto_colorido(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    console.print(f"[bold green]{conteudo}[/bold green]")

def texto_alerta(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    console.print(f"[bold red]⚠ {conteudo}[/bold red]")
