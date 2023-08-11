from ..Produtos.ProdutoPadrão import ProdutoPadrao
from .Ordenador import Ordenador

#filtros
FILTRO_TODOS = "todos"
FILTRO_ESTOQUE_MENOR_OU_IQUAL_A = "estoque_menor_igual"
FILTRO_CATEGORIA_IGUAL_A = "categoria_igual"

#excessão para o filtro não existir
class FiltroNãoExisteException(Exception):

    def __init__(self, message):
        super().__init__(message)    


class GeradorRelatorios:

    def __init__(self, lista_produtos, criterio = "preco_c", filtro="estoque_menor_igual", arg_filtro= "5", format_flags= None):
        self._lista_produtos = lista_produtos
        self._criterio = criterio
        self._filtro = filtro
        self._arg_filtro = arg_filtro
        self._format_flags = format_flags


    @property
    def arg_filtro(self):
        return self._arg_filtro
    
    @property
    def lista_produtos(self):
        return self._lista_produtos
    
    @property
    def criterio(self):
        return self._criterio
    
    @property
    def filtro(self):
        return self._filtro

    @staticmethod
    def debug(arg_filtro, comprimento):
        print(f"Gerando relatório para array contendo {comprimento} produtos...")
        print(f"Parametro filtro - {arg_filtro}.")
        print("...")


    def gera_relatorio(self, arquivo_saida):

        try:
            with open(arquivo_saida, "w+") as file:
                file.write("<!DOCTYPE html><html>\n")
                file.write("<head><title>Relatorio de produtos</title></head>\n")
                file.write("<body>\n")
                file.write("Relatorio de Produtos:\n")
                file.write("<ul>\n")
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo não foi encontrado!")

        comprimento = len(self.lista_produtos)
        
        self.debug(self.arg_filtro, comprimento)

        lista_ordenada = Ordenador().ordena_lista_produtos(self.lista_produtos, self.criterio, 0, len(self.lista_produtos) - 1)
        
        contador = 0

        try: 
             with open(arquivo_saida, "a") as file:

                for produto in lista_ordenada:
                    selecionado = False

                    if self.filtro == FILTRO_TODOS:
                        selecionado = True
                    elif self.filtro == FILTRO_ESTOQUE_MENOR_OU_IQUAL_A:
                        if produto.qtdEstoque <= int(self.arg_filtro): selecionado = True
                    else:
                        raise FiltroNãoExisteException("Filtro Inválido")

                    if selecionado:
                        file.write("<li>\n")
                        file.write("<span style=\"font-weight:bold\">")
                        file.write(produto.formataParaImpressão())
                        file.write("</span>\n")
                        file.write("</li>\n")
                        file.write("<br>")
                        contador += 1
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo não foi encontrado!")
        
        try: 
             with open(arquivo_saida, "a") as file:

                file.write(f'{contador} produtos listados, de um total de {len(lista_ordenada)}.')
                file.write("</ul>")
                file.write("</body>")
                file.write("</html>")
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo não foi encontrado!")
        
        print("Relatório gerado com sucesso!")
        file.close()

        
            