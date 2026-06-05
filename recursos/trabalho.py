import pygame

def sol_pulsante(tela, x, y, raio):
    pygame.draw.circle(tela, (255,215,0), (x,y), raio)
    pygame.draw.circle(tela, (255,255,100), (x,y), int(raio * 0.7))