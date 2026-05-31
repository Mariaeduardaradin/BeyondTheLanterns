import pygame
pygame.init()

tamanho = (1000,700)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Beyond The Lanterns")
icone = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
branco = (255, 255, 255)
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
    
    tela.fill(branco)
    pygame.display.update()
    relogio.tick(60)
pygame.quit()
