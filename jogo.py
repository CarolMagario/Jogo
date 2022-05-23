import pygame 
from pygame.locals import *

pygame.init()
 
screen = pygame.display.set_mode((576,1024))
fps = pygame.time.Clock()

#Declarar variáveis
acabou = False
pulo = False 

#Loop principal do jogo
while not acabou :
    #processar eventos do mouse e do teclado
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                acabou = True 
            if event.key == K_SPACE:
                pulo = True
        if event.type == MOUSEBUTTOMDOWN:
            pulo = True
    #lógica do jogo
    #desenhar gráficos
    pygame.display.update()
    fps.tick(25)

#fim do loop, fim do jogo
pygame.quit()
