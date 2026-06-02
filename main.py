import pygame
from recursos.funcoes import limpar_tela, inicializar_log, salvar_log, maior_pontuador

limpar_tela()
inicializar_log()
pygame.init()

while True:
    nome = input("Identifique-se, cidadão de Corona: ")
    if len(nome) > 0:
        break
    else:
        print("A guarda real não aceita esses caracteres.")

tamanho = (1000,700)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Beyond The Lanterns")
icone = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
branco = (255, 255, 255)
preto = (0, 0, 0)

menu = pygame.image.load("bases/menu.jpg")
menu = pygame.transform.scale(menu, (1000,700))

def tela_inicio():
    maiorNome, maiorPontos, dataJogada, horaJogada = maior_pontuador()
    botaoIniciar = pygame.Rect(350, 540, 300, 80)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botaoIniciar.collidepoint(evento.pos):
                        return

        tela.blit(menu, (0,0))
        fonteTitulo = pygame.font.Font("bases/Tangled.ttf", 110)
        fonte = pygame.font.Font("bases/EBGaramond.ttf", 30)
        titulo2 = fonteTitulo.render("Beyond The Lanterns", True, preto)
        tela.blit(titulo2, (105, 30))
        titulo = fonteTitulo.render("Beyond The Lanterns", True, (255,215,0))
        tela.blit(titulo, (110, 25))
        textoNome = fonte.render(f"Jogador: {nome}", True, branco)
        tela.blit(textoNome, (50,250))
        textoRecorde = fonte.render(f"Maior Pontuador: {maiorNome}", True, branco)
        tela.blit(textoRecorde, (50,340))
        textoPontos = fonte.render(f"Pontos: {maiorPontos}", True, branco)
        tela.blit(textoPontos, (50,380))
        textoData = fonte.render(f"{dataJogada} - {horaJogada}", True, branco)
        tela.blit(textoData, (50,440))
        textoExplicacao = fonte.render("Colete lanternas e desvie dos obstáculos", True, branco)
        tela.blit(textoExplicacao, (545, 650))        
              
        mouse = pygame.mouse.get_pos()
        if botaoIniciar.collidepoint(mouse):
                corBotao = (180, 0, 180)
        else:
                corBotao = (128, 0, 128)

        botaoIniciar = pygame.draw.rect(tela, corBotao, botaoIniciar, border_radius=15)
        textoBotao = fonte.render("INICIAR JOGO", True, (255,215,0))
        tela.blit(textoBotao, (400, 560))

        pygame.display.update()
        relogio.tick(60)

tela_inicio()    

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
