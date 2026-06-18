class Smartphone:
    def __init__(self, marca):
        self._marca = marca
        self._bateria_percentual = 100

    # Métodos de controle de acesso
    @property
    def marca(self):
        return self._marca
    
    @property
    def bateria_percentual(self):
        return self._bateria_percentual

    @marca.setter
    def marca(self, nova_marca):
        if len(nova_marca.strip()) > 0:
            self._marca = nova_marca.strip()
            return
        raise ValueError('Informe marca com +1 caractere')

    @bateria_percentual.setter
    def bateria_percentual(self, novo_percentual):
        if novo_percentual > 0:
            self._bateria_percentual = novo_percentual

    # Método especial que retorna um texto ao invés do valor de referência do objeto.
    def __str__(self):
        return self._marca
