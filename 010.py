import pygame as pg
pg.init()


tamanho = (1280,650)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("movimentando imagens")

fundo = pg.image.load("espaço.jpeg")
nave = pg.image.load("nave.png")
#remove esta imagem do desenho
nave.set_colorkey((255,255,255))
#visibilidade do mouse


pg.mouse.set_visible(0)

vel=pg.time.Clock()

sobre_x = 0
sobre_y = 0

sair = False
while not sair:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sair = True
    # tela de fundo
    tela.blit(fundo , (0,0))

    # movimento da nave + nave
    cord = pg.mouse.get_pos()
    tela.blit(nave , (cord))

    #velocidade do movimento
    vel.tick(60)

    pg.display.flip()