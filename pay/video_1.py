import pygame
from pygame.locals import * #dentro do meu sub modulo locals eu vou ta importando todas as funcões e constantes
from sys import exit #essa funão vai ser chamada e vai fechar a janela

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SHOW DO MILHÃO')

fundo = pygame.image.load('Show_do_Milhão_Logo_2024.jpg')
tela.blit(fundo, (180, 150))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   
        pygame.display.update()
