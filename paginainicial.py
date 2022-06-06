#Página inicial
from turtle import window_height
import pygame, sys
from pygame.locals import *
import random as r

pygame.init()
window = pygame.display.set_mode((500, 400))
fontepeq= pygame.font.SysFont("Arial", 25)
fontemed= pygame.font.SysFont("Arial", 50)
fontegran= pygame.font.SysFont("Arial", 80)
def introdojogo():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    intro=False
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
    gameDisplay.fill("white")
    mensagem("FLAPPY FOX",
            orange,
            -100,
            "large")
    mensagem("Está pronto para embarcar nessa aventura?",
            black,
            -30)
    mensagem("Clique no espaço para movimentar a raposa e ajuda-la a superar os seus desafios",
            black,
            10)
    mensagem("Caso precise sair, aperte a tecla esc",
            black,
            50)
    mensagem("Desenvolvido por Carol e Marina",
            black, 
            180)
    pygame.display.update()
    clock.tick(15)
introdojogo()