import pygame as pg,sys
pg.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("detectando colisões")

x = 0
vel = pg.time.Clock()

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    x+=1
    tela.fill(preto)
    f1=pg.draw.rect(tela,azul,(x,200,100,100))
    f2=pg.draw.rect(tela,azul,(600,200,100,100))
    if f1.colliderect(f2):
        x=100
    pg.display.flip()
    vel.tick(100)


