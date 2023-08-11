import csv

from ..Produtos.ProdutoPadrão import ProdutoPadrao

#excessão para arquivo não encontrado
class ArquivoNãoEncontradoException(Exception):

    def __init__(self, message):
        super().__init__(message)

class CarregaProdutos:

    @staticmethod
    def leitura_csv(file):

        try:
            with open(file) as csv_file:
                
                csv_reader = csv.reader(csv_file, delimiter=',')

                csv_reader.__next__()

                lista_produtos = []

                for row in csv_reader:

                    produto = ProdutoPadrao(row[0], row[1], row[2], row[3], row[4])
                    lista_produtos.append(produto)
                    
            csv_file.close()
            return lista_produtos    
        
        except FileNotFoundError:
            raise ArquivoNãoEncontradoException('O arquivo passado não pode ser encontrado')