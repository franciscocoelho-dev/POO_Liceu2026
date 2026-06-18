class Musica:
    def __init__(self, titulo: str, artista: str) -> None:
        self._titulo: str = titulo
        self._artista: str = artista

    # Métodos de acesso aos atributos
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def artista(self) -> str:
        return self._artista
    
    @titulo.setter
    def titulo(self, novo_titulo: str) -> None:
        if len(novo_titulo.strip()) < 1:
            raise ValueError('Titulo deve ter +1 caractere')
            return
        self._titulo = novo_titulo.strip()

    @artista.setter
    def artista(self, novo_artista: str) -> None:
        if len(novo_artista.strip()) < 1:
            raise ValueError('Artista deve ter +1 caractere')
            return
        self._titulo = novo_artista.strip()

    def __str__(self) -> str:
        return self.titulo

    def __repr__(self) -> str:
        return self.__str__()
    
    def __del__(self):
        print(f'{self.titulo} foi deletada')

