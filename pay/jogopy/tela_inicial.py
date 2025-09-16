import pygame
from pygame.locals import * #dentro do meu sub modulo locals eu vou ta importando todas as funcões e constantes
from sys import exit #essa funão vai ser chamada e vai fechar a janela

pygame.init()

musica_de_fundo = pygame.mixer.music.load('BoxCat Games_Victory.mp3')
pygame.mixer.music.play(-1)

som_dinheiro = pygame.mixer.Sound('smw_switch_timer_ending.wav')

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SHOW DO MILHÃO')

fundo = pygame.image.load('cordel.png')
tela.blit(fundo, (0, 0))

#fonte = pygame.font.SysFonte('arial', 40, True)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   
        pygame.display.update()
 