import pygame, sys

class Fundo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.tamanho_ideal_raposa = (35,47.5)
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_02_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_03_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_04_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_05_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_06_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_07_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_08_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_09_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_10_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_11_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_12_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_13_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_14_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_15_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_16_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('frame_17_delay-0.129s.png'),self.tamanho_ideal_raposa))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        self.animate()

    def animate(self):
        self.is_animating = True
    def update(self):
        
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite>= len(self.sprites):
                self.current_sprite = 0
                #self.is_animating = False #faz com que ocorra apenas uma vez a animação
            self.image = self.sprites[int(self.current_sprite)]