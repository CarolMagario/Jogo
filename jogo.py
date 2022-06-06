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
pulo = False 
cano = [50,200] # localização no eixo x dos dois canos, localização no eixo y do topo do cano
raposa = [50,0]
movimento=0
################
#Animação 
class Animation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('raposinha1.png'))
        self.sprites.append(pygame.image.load('raposinha2.png'))
        self.sprites.append(pygame.image.load('raposinha3.png'))
        self.sprites.append(pygame.image.load('raposinha4.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite>= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False #faz com que ocorra apenas uma vez a animação
            self.image = self.sprites[int(self.current_sprite)]

pygame.init()
clock = pygame.time.Clock()

screen_width = 100
screen_height = 100
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
raposinha = Animation(50,50)
moving_sprites.add(raposinha)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            raposinha.animate()


    screen.fill((250,250,250))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(100)
    

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
