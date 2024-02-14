import pygame as pg
import sys
pg.init() #inicializa a biblioteca


#cria uma tela
tamanho = (200,200)
tela = pg.display.set_mode(tamanho)

#sistema para que a tela se feche.
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()

