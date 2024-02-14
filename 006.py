import pygame as pg,sys
pg.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("implementando mouse")
vel = pg.time.Clock()
pg.mouse.set_visible(0)

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    lista = []
    pos = pg.mouse.get_pos()
    print(pos)
    tela.fill(preto)
    pg.draw.circle(tela,azul,(pos[0],pos[1]),50)
    pg.display.flip()
    vel.tick(20)