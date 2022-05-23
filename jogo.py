from turtle import window_height
import pygame 
from pygame.locals import *

pygame.init()
 
screen = pygame.display.set_mode((600,800))
fps = pygame.time.Clock()

#Declarar variáveis
BACKGROUND = pygame.image.load("Jogo/Imagens/33HF.gif").convert_alpha()

raposa = pygame.image.load("Jogo/Imagens/fox2_preview_rev_1.png").convert_alpha()
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
        if event.type == MOUSEBUTTONDOWN:
            pulo = True

    #lógica do jogo

    #desenhar gráficos
    screen.fill((0,0,0))
    screen.blit(BACKGROUND, (0,0)) #background
    screen.blit(raposa, (200,200))
    #base
    #canos
    #bichinho
    pygame.display.update()
    fps.tick(25)

#fim do loop, fim do jogo
pygame.quit()
