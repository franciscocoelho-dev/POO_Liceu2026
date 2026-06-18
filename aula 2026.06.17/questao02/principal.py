from playlist import Playlist
from musica import Musica

m1 = Musica('O Sol do Verão', 'Maria')
m2 = Musica('A Chuva do Inverno', 'João')

p1 = Playlist('Escolhidas')
p1.adicionar_musica(m1)
p1.adicionar_musica(m2)

print(p1.lista_musica)


print('-' * 40)
del p1
print('-' * 40)



