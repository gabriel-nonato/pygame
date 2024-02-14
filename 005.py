import pygame as pg , sys , random,time
pg.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

tamanho = (800,600)
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("chuva")
vel = pg.time.Clock()


lista = []

for ponto in range(100):
    x = random.randint(0,800)
    y = random.randint(0,600)
    lista.append([x,y])

cord_x = 0
cord_y = 200

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
    cord_x+=10
    cord_y+=2


    tela.fill(preto)
    for cord in lista: #cord[0] = x , cord[1] = y
        pg.draw.circle(tela,azul,cord,1)
        cord[0]+=1
        if cord[0] == 800:
            cord[0] = 0
    pg.draw.circle(tela,vermelho,(cord_x,cord_y),50)

    pg.display.flip()
    vel.tick(10)