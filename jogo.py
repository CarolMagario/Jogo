from turtle import window_height
import pygame
from pygame.locals import *
import random as r

pygame.init() 

screen_largura = 600
screen_altura = 800
screen = pygame.display.set_mode((screen_largura,screen_altura))
fps = pygame.time.Clock()

#Página inicial


#Declarar variáveis
BACKGROUND = pygame.image.load("./Imagens/33HF.gif").convert_alpha()
BASE = pygame.image.load("./Imagens/ground.png").convert_alpha()
raposa = pygame.image.load("./Imagens/fox2_preview_rev_1.png").convert_alpha()
#canos sem dimensão
CANO_debaixo =  pygame.image.load('./cano2.png').convert_alpha()
CANO_de_cima = pygame.transform.flip(CANO_debaixo, False, True).convert_alpha()
#canos dimensionados
tamanho_ideal = (100,550)
CANO_top = pygame.transform.scale(CANO_de_cima,tamanho_ideal)
CANO_bottom = pygame.transform.scale(CANO_debaixo,tamanho_ideal)
cano_altura = 600
cano_buraco = r.randint(150,300) 
cano_velocidade = 7
cano_largura = 52
# Bichinho
Raposa = pygame.image.load("./Imagens/raposinha.png").convert_alpha()
tamanho_ideal_raposa = (200,95)
RAPOSA = pygame.transform.scale(Raposa,tamanho_ideal_raposa)
raposa_animaçao = 0
###########
acabou = False
inicio=False
pulo = False 
cano = [50,200] # localização no eixo x dos dois canos, localização no eixo y do topo do cano
raposa = [50,0]
movimento=0
lives=4
#inicio
while not inicio:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                inicio= True 
                

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
    if pulo:
        movimento= 20
        pulo=False
    raposa[1] -= movimento
    if movimento>-20:
        movimento -= 2
    cano[0] -= cano_velocidade
    if cano[0] < -cano_largura:
        cano[0] = screen_largura
        cano[1] = r.randint(150,screen_altura - 150) 
        
    #desenhar gráficos
    screen.fill((0,0,0))

    #background
    screen.blit(BACKGROUND, (0,0)) 
    
    #base
    screen.blit(BASE,(0,700))

    #canos
    screen.blit(CANO_top, (cano[0], cano[1]-cano_altura))
    screen.blit(CANO_bottom, (cano[0], cano[1]+cano_buraco/2))

    #bichinho
    screen.blit(RAPOSA, raposa, (0,raposa_animaçao*190,50,190))
    raposa_animaçao += 1
    if raposa_animaçao > 4:
        raposa_animaçao = 0
    pygame.display.update()
    fps.tick(25)

    #colisão bichinho e cano
    cano_top_rect = CANO_top.get_rect(topleft=(cano[0], cano[1]-cano_altura))
    cano_bottom_rect= CANO_bottom.get_rect(topleft=(cano[0], cano[1]+cano_buraco/2))
    raposa_rect= Rect(raposa[0], raposa[1], 50, 190)

    if raposa_rect.colliderect(cano_bottom_rect) or raposa_rect.colliderect(cano_top_rect):
        #Colisão
        lives-=1
        raposa = [50,0]

        if lives==0:
            finished=True

    #atualizar tela
    pygame.display.update()
    fps.tick(25)
#fim do loop, fim do jogo
pygame.quit()
