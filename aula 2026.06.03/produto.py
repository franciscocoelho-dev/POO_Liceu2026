class Produto:
    def __init__(self, descricao, quantidade, valor):
        self._descricao = descricao
        self._quantidade = quantidade
        self._valor = valor

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if not isinstance(nova_quantidade, int) or nova_quantidade < 0:
            raise ValueError('Nova quantidade deve ser inteiro e maior que 0')
        self._quantidade += nova_quantidade 


p1 = Produto('Cadeira Gamer', 20, 990.00)
p1.quantidade = 10
print(p1.quantidade)





