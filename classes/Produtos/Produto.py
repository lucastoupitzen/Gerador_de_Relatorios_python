from abc import ABCMeta, abstractproperty

class Produto(metaclass=ABCMeta):

    @abstractproperty
    def setQtdEstoque(self):
        pass

    @abstractproperty
    def setPreço(self):
        pass

    @abstractproperty
    def setCategoria(self):
        pass

    @abstractproperty
    def setDescrição(self):
        pass

    @abstractproperty
    def setId(self):
        pass

    @abstractproperty
    def id(self):
        pass

    @abstractproperty
    def descrição(self):
        pass

    @abstractproperty
    def categoria(self):
        pass

    @abstractproperty
    def qtdEstoque(self):
        pass

    @abstractproperty
    def preço(self):
        pass

    @abstractproperty
    def formataParaImpressão(self):
        pass

    
    

