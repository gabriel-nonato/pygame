import pygame as pg
import time
pg.init()

fundo = pg.image.load("espiral.GIF")
fundo2 = pg.image.load("estrelado.jpg")



tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("adicionando imagens de fundo")


sair = True

while sair :
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
             sair = False
        tela.blit(fundo,(0,0))

    pg.display.flip()
pg.quit()