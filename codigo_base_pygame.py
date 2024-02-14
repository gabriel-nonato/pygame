import pygame as pg
pg.init()

#---cores---#
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
#---cores---#

#tela
tamanho = (400,500)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("você esta telando a tela!!!")

vel = pg.time.Clock() #velocidade dos eventos +


#fechar tela
sair = True
while sair:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sair = False
        #---Área de detecção do teclado---#

        #---Área de detecção do teclado---#


    #---Área de logica---#

    #---Área de logica---#

    #cor da tela
    tela.fill(branco)

    #---Área de desenho---#

    #---Área de desenho---#

    pg.display.flip() #atualização da tela
    vel.tick(20) #velocidade dos eventos

pg.quit()
