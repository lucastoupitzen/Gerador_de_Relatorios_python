from classes.Gerador.CarregaProdutos import CarregaProdutos
from classes.Gerador.GeradorRelatorios import GeradorRelatorios
import sys

def main():

    lista_produtos = CarregaProdutos().leitura_csv('produtos.csv')
    gerador = GeradorRelatorios(lista_produtos, sys.argv[1], sys.argv[2], sys.argv[3])
    gerador.gera_relatorio("index.html")




main()