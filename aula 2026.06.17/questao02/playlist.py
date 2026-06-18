from typing import List
from musica import Musica

class Playlist:
    def __init__(self, nome: str) -> None:
        self._nome: str = nome
        self._lista_musica: List[Musica] = []
    
    # Métodos de acesso aos atributos
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def lista_musica(self) -> List:
        return self._lista_musica

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if len(novo_nome.strip()) < 1:
            raise ValueError('Nome deve ter +1 caractere')
            return
        self._nome = novo_nome
        
    # Métodos da Regra de Negócio (RN)
    def adicionar_musica(self, musica: Musica) -> None:
        if not isinstance(musica, Musica):
            ''' O uso do isinstance verifica se musica recebido no parâmetro NÃ0 É um objeto do tipo Musica '''
            
            raise ValueError('Necessário ser um objeto do tipo Música')
            return
        self._lista_musica.append(musica)
        

    def __del__(self):
        print(f'{self.nome} foi deletada')

        