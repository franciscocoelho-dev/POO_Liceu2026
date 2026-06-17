# No arquivo (módulo) smartphone importe a class Smartphone
from smartphone import Smartphone

class Motorista:
    def __init__(self, nome):
        self._nome = nome
        self._smartphone = None

    # Métodos de controle de acesso
    @property
    def nome(self):
        return self._nome

    @property
    def smartphone(self):
        return self._smartphone

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome.strip()) > 0:
            self._nome = novo_nome.strip()

    # Métodos da Regra de Negócio
    def conectar_aparelho(self, aparelho):
        ''' O método conectar_aparelho() substitui o
            @_smartphone.setter() '''
        if isinstance(aparelho, Smartphone):
            self._smartphone = aparelho
        