import pygame as pg , sys
from time import sleep
pg.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("telando a tela!")

cord_x = 30
cord_y = 0

desl_x = 3
desl_y = 2

vel = pg.time.Clock()

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    if cord_x > 800 or cord_x < 0:
         desl_x *= -1
    if cord_y >600 or cord_y < 0 :
        desl_y*=-1

    cord_x+=desl_x
    cord_y+=desl_y

    tela.fill(branco)


    pg.draw.circle(tela,preto,(cord_x,cord_y),30)

    pg.display.flip()
    vel.tick(100)