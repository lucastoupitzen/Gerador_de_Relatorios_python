from .Produto import Produto
import locale

class ProdutoPadrao(Produto):
        
    def __init__(self, id, descrição, categoria, qtd_estoque, preço):
        self._id = id
        self._descrição = descrição
        self._categoria = categoria
        self._qtd_estoque = qtd_estoque
        self._preço = preço

    @property
    def id(self):
        return self._id

    @property
    def descrição(self):
        return self._descrição

    @property
    def categoria(self):
        return self._categoria

    @property
    def preço(self):
        return float(self._preço[1:])

    @property
    def qtdEstoque(self):
        return int(self._qtd_estoque[1:])
    
    def setPreço(self, preço):
        self._preço = preço

    def setQtdEstoque(self, qtd_estoque):
        self._qtd_estoque = qtd_estoque

    def setId(self, id):
        self._id = id

    def setCategoria(self, categoria):
        self._categoria = categoria

    def setDescrição(self, descrição):
        self._descrição = descrição

    def formataParaImpressão(self):

        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

        separador = ' ,'
        #pre = locale.currency(self.preço())
        return f'{self.descrição} {separador} {self.categoria} { separador} {str(self.preço)} {separador} {self.qtdEstoque} unidade(s) em estoque'