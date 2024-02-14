# https://www.pygame.org/docs/ref/key.html

import pygame as pg,sys

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("tela_principal")
vel =pg.time.Clock()

pg.mouse.set_visible(0)

x = 300
y = 200
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()

        #---MOVENDO O QUADRADO COM O TECLADO---#
        if evento.type == pg.KEYDOWN:
            if evento.key ==pg.K_UP :
                y -= 20
            if evento.key == pg.K_DOWN:
                y += 20
            if evento.key == pg.K_RIGHT:
                x += 20
            if evento.key == pg.K_LEFT :
                x -= 20
        if evento.type == pg.KEYUP:
            if evento.key == pg.K_UP:
                y -= 20
            if evento.key == pg.K_DOWN:
                y += 20
            if evento.key == pg.K_RIGHT:
                x += 20
            if evento.key == pg.K_LEFT:
                x -= 20

        # ---MOVENDO O QUADRADO COM O TECLADO---#



        #---LIMITE DE TELA---#
        if y > 600:
            y = -90
        elif y < -90:
            y = 600
        if x > 800:
            x = -90
        if x < -90:
            x = 800
        #---LIMITE DE TELA---#

    tela.fill(preto)
    pg.draw.rect(tela,vermelho,(x,y,100,100))
    pg.display.flip()
    vel.tick(20)