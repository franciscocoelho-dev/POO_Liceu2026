# Crie uma class ContaCorrente com os atributos numero, saldo e titular; os métodos devem ser sacar(), depositar(), transferir(), consultar_saldo().

# Implemente os decoradores property e setter para que o saldo não seja modificado diretamente.

from cliente import Cliente

class ContaBancaria:
    def __init__(self, titular: Cliente):
        # Aciona na atribuição o titular() do @setter
        self._titular: Cliente = titular
        self._saldo: float = 0
        
    @property
    def titular(self) -> Cliente:
        return self._titular
    
    @titular.setter
    def titular(self, novo_titular: Cliente) -> None:
        if isinstance(novo_titular, Cliente):
            self._titular = novo_titular
        raise ValueError('Nome deve ser str maior que 5 caracteres')

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser maior que zero')
        elif valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser maior que zero')
        self._saldo += valor
 
