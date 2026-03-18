"""
Módulo responsável por funcionalidades de progresso usando rich.
"""
from rich.progress import track
from rich.console import Console
import time

console = Console()

def ler_conteudo(texto, isArquivo):
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            return f.read()
    return texto

def progresso_simples(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    for _ in track(range(5), description="Processando..."):
        time.sleep(0.2)
    console.print(conteudo)

def progresso_lento(texto, isArquivo):
    conteudo = ler_conteudo(texto, isArquivo)
    for _ in track(range(10), description="Carregando..."):
        time.sleep(0.2)
    console.print(conteudo)
