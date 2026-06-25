class Pagina:

    # Método de Inicialização dos Atributos
    def __init__(self, numero: int, conteudo: str) -> None:
        self._numero = numero
        self._conteudo = conteudo

    # Métodos de Controle de Acesso
    @property
    def numero(self) -> int:
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero: int) -> None:
        if novo_numero < 1:
            raise ValueError('Número da Página deve ser maior que zero')
        self._numero = novo_numero

    @property
    def conteudo(self) -> str:
        return self._conteudo
    
    @conteudo.setter
    def conteudo(self, novo_conteudo: str) -> None:
        if len(novo_conteudo.strip()) < 1:
            raise ValueError('Conteúdo deve ter ao menos 1 caractere')
        self._conteudo = self.conteudo


