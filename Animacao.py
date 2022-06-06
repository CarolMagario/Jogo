import pygame, sys

class Raposa(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        tamanho_ideal_raposa = (140,190)
        self.sprites.append(pygame.transform.scale(pygame.image.load('raposinha1.png'),tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('raposinha2.png'),tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('raposinha3.png'),tamanho_ideal_raposa))
        self.sprites.append(pygame.transform.scale(pygame.image.load('raposinha4.png'),tamanho_ideal_raposa))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        self.animate()

    def animate(self):
        self.is_animating = True
    def update(self):
        
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite>= len(self.sprites):
                self.current_sprite = 0
                #self.is_animating = False #faz com que ocorra apenas uma vez a animação
            self.image = self.sprites[int(self.current_sprite)]

# pygame.init()
# clock = pygame.time.Clock()

# screen_width = 500
# screen_height = 500
# screen = pygame.display.set_mode((screen_width,screen_height))
# pygame.display.set_caption("Sprite Animation")
#     def draw(self,screen):
#         # screen.fill((250,250,250))
#         moving_sprites.draw(screen)
#         moving_sprites.update()
#         pygame.display.flip()
#         # clock.tick(100)
# # moving_sprites = pygame.sprite.Group()
# # # raposinha = Raposa(50,50)
# # moving_sprites.add(raposinha)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN: 
#             raposinha.animate()


    