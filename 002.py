# https://www.pygame.org/docs/ref/draw.html

import pygame as pg
import sys
pg.init()

tamanho= (400,500)
tela=pg.display.set_mode(tamanho)

#cores sistema rgb
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0 ,255)
verde = (0, 255, 0)
rosa = (255, 105 ,179)
vermelho = (255, 0 , 0)

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    #preenche a tela de uma determidada cor
    tela.fill(branco)
    #dentro deste espaço ficara os desenhos feitos na tela
    #------espaço.inicio-----#

    # corpo
    # parametros rect (inicio horizontal, inicio vertical ,lardura, altura )
    pg.draw.rect(tela, preto,(160 ,120,80,200))
    #cabeça
    pg.draw.circle(tela, rosa, (200, 100), 50)
    #pernas
    pg.draw.rect(tela,verde,(160,320,34.7,100))
    pg.draw.rect(tela,azul,(206,320,34.7,100))
    #braços
    pg.draw.rect(tela,azul,(130, 150 , 30 ,150 ))
    pg.draw.rect(tela,verde,(240,150,30,150))
    #olhos
    pg.draw.circle(tela,azul,(180,90),5)
    pg.draw.circle(tela,azul, (225,90),5 )
    #boca
    pg.draw.arc(tela, vermelho, (175, 120, 50, 20), 3, 0.1, 5)




    #-------espaço.fim-------#
    # constantemente atualiza a tela
    pg.display.flip()
