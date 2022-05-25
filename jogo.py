from turtle import window_height
import pygame 
from pygame.locals import *

pygame.init()
 
screen = pygame.display.set_mode((600,800))
fps = pygame.time.Clock()

#Declarar variáveis
BACKGROUND = pygame.image.load("Jogo/Imagens/33HF.gif").convert_alpha()
BASE = pygame.image.load("Jogo/Imagens/ground.png").convert_alpha()
raposa = pygame.image.load("Jogo/Imagens/fox2_preview_rev_1.png").convert_alpha()
#canos sem dimensão
CANO_debaixo =  pygame.image.load("Jogo/Imagens/cano.png").convert_alpha()
CANO_de_cima = pygame.transform.flip(CANO_debaixo, False, True).convert_alpha()
#canos dimensionados
tamanho_ideal = (240,460)
CANO_top = pygame.transform.scale(CANO_de_cima,tamanho_ideal)
CANO_bottom = pygame.transform.scale(CANO_debaixo,tamanho_ideal)
cano_altura = 260
cano_buraco = 300

acabou = False
pulo = False 
cano = [200,100] # localização no eixo x dos dois canos, localização no eixo y do topo do cano

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

    #background
    screen.blit(BACKGROUND, (0,0)) 
    
    #base
    screen.blit(BASE,(0,700))

    #canos
    screen.blit(CANO_top, (cano[0], cano[1]-cano_altura))
    screen.blit(CANO_bottom, (cano[0], cano[1]+cano_buraco))

    #bichinho
    screen.blit(raposa, (200,200))
    pygame.display.update()
    fps.tick(25)

#fim do loop, fim do jogo
pygame.quit()
