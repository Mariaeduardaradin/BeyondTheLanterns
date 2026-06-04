import pygame
import random
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
fundo = pygame.image.load("bases/fundo.jpg")
fundo = pygame.transform.scale(fundo, (1000,700))
pascal = pygame.image.load("bases/pascal.png")
pascal = pygame.transform.scale(pascal, (105,75))
lanterna = pygame.image.load("bases/lanterna.png")
lanterna = pygame.transform.scale(lanterna, (42,60))
flor = pygame.image.load("bases/flor.png")
flor = pygame.transform.scale(flor, (40,60))

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


def jogo():
    fundoX1 = 0
    fundoX2 = 1000
    velocidadeFundo = 3
    posicaoXPascal = 135
    linhas = [232,308,390,470,557]
    linhaAtual = 2
    posicaoYPascal = linhas[linhaAtual]
    pontos = 0
    fonteHUD = pygame.font.Font("bases/EBGaramond.ttf", 30)
    posicaoXLanterna = 1200
    posicaoYLanterna = random.choice(linhas)


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()                   
                if evento.key == pygame.K_UP:
                    if linhaAtual > 0:
                        linhaAtual -= 1
                if evento.key == pygame.K_DOWN:
                    if linhaAtual < 4:
                        linhaAtual += 1


        posicaoYPascal = linhas[linhaAtual]
        retanguloPascal = pygame.Rect(posicaoXPascal, posicaoYPascal, 105,75)
        retanguloLanterna = pygame.Rect(posicaoXLanterna, posicaoYLanterna, 42,60)

        if retanguloPascal.colliderect(retanguloLanterna):
            pontos += 1
            posicaoXLanterna = random.randint(1200,1800)
            posicaoYLanterna = random.choice(linhas)
        if pontos >= 10:
            velocidadeFundo = 4
        if pontos >= 20:
            velocidadeFundo = 5
        if pontos >= 30:
            velocidadeFundo = 6

        fundoX1 -= velocidadeFundo
        fundoX2 -= velocidadeFundo
        posicaoXLanterna -= velocidadeFundo
        if fundoX1 <= -1000:
            fundoX1 = 1000
        if fundoX2 <= -1000:
            fundoX2 = 1000
        if posicaoXLanterna < -100:
            posicaoXLanterna = random.randint(1200,1800)
            posicaoYLanterna = random.choice(linhas)

        tela.blit(fundo, (fundoX1,0))
        tela.blit(fundo, (fundoX2,0))
        tela.blit(lanterna, (posicaoXLanterna, posicaoYLanterna))
        tela.blit(pascal, (posicaoXPascal, posicaoYPascal))
        textoPontos = fonteHUD.render(f"Pontos: {pontos}", True, branco)
        tela.blit(textoPontos, (20,20))

        pygame.display.update()
        relogio.tick(60)


tela_inicio()    
jogo()