#constantes que definem os critérios de ordenação
CRIT_PRECO_CRESC = "preco_c"
CRIT_ESTOQUE_CRESC = "estoque_c"

#excessão lançada por critério inválido
class CriterioInvalidoException(Exception):

    def __init__(self, message):
        super().__init__(message)

#classe responsável por ordenar a lista de produtos utilizando quicksort seguindo critérios 
class Ordenador:

    @staticmethod
    def particiona(lista_produtos, criterio, inicio, fim):

        

        produto = lista_produtos[inicio]
        i = inicio - 1
        j = fim + 1

        while True:

            if criterio == CRIT_PRECO_CRESC:

                j -= 1
                while lista_produtos[j].preço > produto.preço:  
                    j -= 1
                i += 1
                while lista_produtos[i].preço < produto.preço:
                    i += 1
            elif criterio == CRIT_ESTOQUE_CRESC:
                j -= 1
                while lista_produtos[j].qtdEstoque > produto.qtdEstoque:
                    j -= 1
                i += 1
                while lista_produtos[i].qtdEstoque < produto.qtdEstoque:
                    i += 1
            else:
                raise CriterioInvalidoException("Critério de ordenação escolhido não é válido!")
            
            
            if i < j:
                auxiliar = lista_produtos[i]
                lista_produtos[i] = lista_produtos[j]
                lista_produtos[j] = auxiliar
            
            else: return j
        
    def ordena_lista_produtos(self, lista_produtos, criterio, inicio, fim):

        if inicio < fim:
            aux = self.particiona(lista_produtos, criterio, inicio, fim)
            self.ordena_lista_produtos(lista_produtos, criterio, inicio, aux)
            self.ordena_lista_produtos(lista_produtos, criterio, aux + 1, fim)
        
        return lista_produtos