import pygame as pg , sys
pg.init()
#---cores---#
branco = (255, 255, 255)
preto = (0 ,0 ,0)
vermelho = (255, 0, 0)
verde = (0,255,0)
azul = (0 , 0 ,255)
#---cores---#
tamanho = (800,700)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("teste.003")



while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    tela.fill(preto)
    #---desenho---#
    for l in range(100,700, 100):
        for a in range(0,700,100):
            pg.draw.rect(tela,verde,(l,a,50,50))
            pg.draw.circle(tela,vermelho,(l,a),40)
    #---desenho---#
    pg.display.flip()