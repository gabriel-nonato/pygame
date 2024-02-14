import pygame as pg
import time
import PySimpleGUI as ps
pg.init()

preto = (0,0,0)
branco = (255,255,255)

pg.display.set_caption("pong-trapaça")
tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
vel = pg.time.Clock()
velocidade = 100

#---jogador_1---#
x = 750 #constante
y = 250
larg = 20
alt = 100

#---jogador_2---#
x_2 = 30 #constante
y_2 = 250
larg_2 = 20
alt_2 = 100

#---bola---#
x_b = 400
y_b = 300
r_b = 20
#movimento
mov_x = 2
mov_y = 2

#---sistema de pontuação---#
pont_1 = 0
pont_2 = 0


sair = True
while sair:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sair = False
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_DELETE:
                sair=False
            if evento.key == pg.K_UP:
                y -= 30
            if evento.key == pg.K_DOWN:
                y += 30
            if evento.key == pg.K_w:
                y_2 -= 30
            if evento.key == pg.K_s:
                y_2 += 30
            #---Trapaças---#
            if evento.key == pg.K_1:
                r_b += 40





    #---movimento da bola---#
    x_b += mov_x
    y_b += mov_y
    if y_b < 0 or y_b > 600:
        mov_y *= -1

    #---jogador X limite de tela---#
    if y < -90:
        y = 600
    if y > 600:
        y = -90

    if y_2 < -90:
        y_2 = 600
    if y_2 > 600:
        y_2 = -90


    tela.fill(preto)

    jogador_1 = pg.draw.rect(tela, branco, (x, y, larg, alt))

    jogador_2 = pg.draw.rect(tela, branco, (x_2, y_2, larg_2, alt_2))

    bola = pg.draw.circle(tela, branco, (x_b, y_b), r_b)

    #---INTERAÇÃO BOLA E JOGADOR---#
    if  bola.colliderect(jogador_1) or  bola.colliderect(jogador_2):
        mov_x*=-1
    #---sistema de pontuação---#
    if x_b>800:
        x_b = 400
        y_b = 300
        pont_1 +=1
    if x_b<0:
        x_b = 400
        y_b = 300
        pont_2+=1

    pg.display.flip()
    vel.tick(velocidade)
pg.quit()
