from turtle import window_height
import pygame
from pygame.locals import *
import random as r
from Animacao import *
from Fundo import *


pygame.init() 

screen_largura = 600
screen_altura = 800
screen = pygame.display.set_mode((screen_largura,screen_altura))
fps = pygame.time.Clock()
imageminicial=pygame.image.load("./Imagens/pixil-frame-0.png").convert_alpha()
imageminicial = pygame.transform.scale(imageminicial,(600,800))
imagemfinal = pygame.image.load("./Imagens/pixil-frame-0-2.png").convert_alpha()
imagemfinal = pygame.transform.scale(imagemfinal,(600,800))

inicio=False
#Página inicial
while not inicio:
    fps.tick(25)
    screen.blit(imageminicial, (0,0) )
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                inicio= True 

#Declarar variáveis
BACKGROUND = pygame.image.load("./frame_05_delay-0.129s.png").convert_alpha()
BASE = pygame.image.load("./Imagens/ground.png").convert_alpha()
fundo = Fundo(0,700)
moving_sprites = pygame.sprite.Group()
moving_sprites.add(fundo)

# Sons
MORRE = pygame.mixer.Sound("./Imagens/media_hit.wav")
PULA =  pygame.mixer.Sound("./Imagens/pulinho.wav")
#canos sem dimensão
CANO_debaixo =  pygame.image.load('./Imagens/canoazul.png').convert_alpha()
CANO_de_cima = pygame.transform.flip(CANO_debaixo, False, True).convert_alpha()

jogo = True

while jogo:
    #canos dimensionados
    tamanho_ideal = (100,550)
    CANO_top = pygame.transform.scale(CANO_de_cima,tamanho_ideal)
    CANO_bottom = pygame.transform.scale(CANO_debaixo,tamanho_ideal)
    cano_altura = 600
    cano_buraco = r.randint(150,300) 
    cano_velocidade = 7
    cano_largura = 52

    # Bichinho
    raposinha = Raposa(50,50)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(raposinha)
    ###########
    acabou = False
    pulo = False 
    cano = [500,180] # localização no eixo x dos dois canos, localização no eixo y do topo do cano
    raposa = [50,0]
    movimento=0
    lives=4 


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
            movimento= 15 
            pulo=False
            PULA.play()
        raposinha.rect.y -= movimento
        if movimento>-15:
            movimento -= 2
        cano[0] -= cano_velocidade
        if cano[0] < -cano_largura:
            cano[0] = screen_largura
            cano[1] = r.randint(150,screen_altura - 150) 
            
        #desenhar gráficos
        screen.fill((0,0,0))

        #background
        screen.blit(BACKGROUND, (0,0)) 
        # fundo.update()
        # moving_sprites.draw(screen)

        #base
        screen.blit(BASE,(0,700))


        #canos
        screen.blit(CANO_top, (cano[0], cano[1]-cano_altura))
        screen.blit(CANO_bottom, (cano[0], cano[1]+cano_buraco/2))
        

        #bichinho 2.0
        raposinha.update()
        moving_sprites.draw(screen)
    


        #colisão bichinho e cano
        cano_top_rect = CANO_top.get_rect(topleft=(cano[0], cano[1]-cano_altura))
        cano_bottom_rect= CANO_bottom.get_rect(topleft=(cano[0], cano[1]+cano_buraco/2))
        raposa_rect= Rect(raposinha.rect.x, raposinha.rect.y, raposinha.tamanho_ideal_raposa[0],  raposinha.tamanho_ideal_raposa[1 ])
        base_rect = BASE.get_rect(topleft=(0,700))

        if raposa_rect.colliderect(cano_bottom_rect) or raposa_rect.colliderect(cano_top_rect) or raposa_rect.colliderect(base_rect) or raposa_rect.y<-10:
            #Colisão
            
            lives-=1
            raposa = [50,0]

            if lives==0:
                MORRE.play()
                acabou=True

        #atualizar tela
        pygame.display.update()
        fps.tick(25)
        #fim do loop, fim do jogo
        fim=False
    #Página final
    while not fim:
        screen.blit(imagemfinal, (0,0) )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fim= True
                    jogo = False
                    pygame.quit()
                if event.key == K_SPACE:
                    acabou = False
                    fim = True
                    break

pygame.quit()
