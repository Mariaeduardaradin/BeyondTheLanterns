import pygame
import random
import pyttsx3

from recursos.funcoes import limpar_tela, inicializar_log, salvar_log, maior_pontuador
from recursos.trabalho import sol_pulsante

limpar_tela()
inicializar_log()
pygame.init()
narrador = pyttsx3.init()

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
gameover = pygame.image.load("bases/gameover.jpg")
gameover = pygame.transform.scale(gameover, (1000,700))
pascal = pygame.image.load("bases/pascal.png")
pascal = pygame.transform.scale(pascal, (105,75))
lanterna = pygame.image.load("bases/lanterna.png")
lanterna = pygame.transform.scale(lanterna, (42,60))
flor = pygame.image.load("bases/flor.png")
flor = pygame.transform.scale(flor, (46,70))
borboleta = pygame.image.load("bases/borboleta.png")
coracao = pygame.image.load("bases/vidas.png")
coracao = pygame.transform.scale(coracao, (55,55))
pedra1 = pygame.image.load("bases/pedra1.png")
pedra2 = pygame.image.load("bases/pedra2.png")
arbusto = pygame.image.load("bases/arbusto.png")
tronco = pygame.image.load("bases/tronco.png")
listaObstaculos = [pedra1,pedra2,arbusto,tronco]

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
                        narrador.say("Uma nova aventura começa...")
                        narrador.runAndWait()
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
        textoRecorde = fonte.render(f"Recordista: {maiorNome}", True, branco)
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

def game_over(nome, pontos):
    salvar_log(nome, pontos)
    maiorNome, maiorPontos, dataJogada, horaJogada = maior_pontuador()

    fonte = pygame.font.Font("bases/EBGaramond.ttf", 30)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        tela.blit(gameover, (0,0))
        textoMaiorPontuador = fonte.render(f"Maior Pontuador:    {maiorNome}  {maiorPontos} pontos  {dataJogada} - {horaJogada} ", True, branco)
        textoStartAgain = fonte.render("Pressione ENTER para jogar novamente", True, branco)
        tela.blit(textoMaiorPontuador, (10, 15))
        tela.blit(textoStartAgain, (525,630))

        pygame.display.update()
        relogio.tick(60)

def jogo():
    fundoX1 = 0
    fundoX2 = 1000
    velocidadeFundo = 3
    raioSol = 20
    crescendoSol = True
    posicaoXPascal = 135
    linhas = [232,308,390,470,557]
    linhaAtual = 2
    posicaoYPascal = linhas[linhaAtual]
    pontos = 0
    vidas = 3
    tempoInvulneravel = 0
    posicaoXBorboleta = 120
    posicaoYBorboleta = 15
    contadorBorboleta = 0
    pausado = False
    fonteHUD = pygame.font.Font("bases/EBGaramond.ttf", 25)

    posicaoXLanterna = 1200
    posicaoYLanterna = random.choice(linhas)
    posicaoXFlor = random.randint(8000,15000)
    posicaoYFlor = random.choice(linhas)
    posicaoXObstaculo1 = random.randint(1000,1200)
    posicaoYObstaculo1 = random.choice(linhas)
    posicaoXObstaculo2 = random.randint(1200,1400)
    posicaoYObstaculo2 = random.choice(linhas)
    posicaoXObstaculo3 = random.randint(1400,1700)
    posicaoYObstaculo3 = random.choice(linhas)
    obstaculoAtual1 = random.choice(listaObstaculos)
    obstaculoAtual2 = random.choice(listaObstaculos)
    obstaculoAtual3 = random.choice(listaObstaculos)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if evento.key == pygame.K_SPACE:
                    pausado = not pausado 
                if evento.key == pygame.K_UP:
                    if linhaAtual > 0:
                        linhaAtual -= 1
                if evento.key == pygame.K_DOWN:
                    if linhaAtual < 4:
                        linhaAtual += 1

        if pausado:
            textoPause = fonteHUD.render("JOGO PAUSADO", True, branco)
            textoSpace = fonteHUD.render("Press Space to Continue", True, branco)
            tela.blit(textoPause, (412,330))
            tela.blit(textoSpace, (388,370))

            pygame.display.update()
            relogio.tick(60)
            continue

        posicaoYPascal = linhas[linhaAtual]
        if tempoInvulneravel > 0:
            tempoInvulneravel -= 1
        retanguloPascal = pygame.Rect(posicaoXPascal, posicaoYPascal, 105,75)
        retanguloLanterna = pygame.Rect(posicaoXLanterna, posicaoYLanterna, 42,60)
        retanguloObstaculo1 = pygame.Rect(posicaoXObstaculo1,posicaoYObstaculo1, 55,55)
        retanguloObstaculo2 = pygame.Rect(posicaoXObstaculo2, posicaoYObstaculo2, 55,55)
        retanguloObstaculo3 = pygame.Rect(posicaoXObstaculo3, posicaoYObstaculo3, 55,55)
        retanguloFlor = pygame.Rect(posicaoXFlor, posicaoYFlor, 40,60)

        if retanguloPascal.colliderect(retanguloLanterna):
            pontos += 1
            posicaoXLanterna = random.randint(1000,1500)
            posicaoYLanterna = random.choice(linhas)
            while ((posicaoYLanterna == posicaoYObstaculo1 and abs(posicaoXLanterna - posicaoXObstaculo1) < 250) or (posicaoYLanterna == posicaoYObstaculo2 and abs(posicaoXLanterna - posicaoXObstaculo2) < 250) or (posicaoYLanterna == posicaoYObstaculo3 and abs(posicaoXLanterna - posicaoXObstaculo3) < 250) or (posicaoYLanterna == posicaoYFlor and abs(posicaoXLanterna - posicaoXFlor) < 250)):
                posicaoXLanterna = random.randint(1000,1500)
                posicaoYLanterna = random.choice(linhas)
        if retanguloPascal.colliderect(retanguloFlor):
            pontos += 5
            posicaoXFlor = random.randint(8000,15000)
            posicaoYFlor = random.choice(linhas)
            while ((posicaoYFlor == posicaoYObstaculo1 or posicaoYFlor == posicaoYObstaculo2 or posicaoYFlor == posicaoYObstaculo3) or (posicaoYFlor == posicaoYLanterna and abs(posicaoXFlor - posicaoXLanterna) < 250)):
                posicaoXFlor = random.randint(8000,15000)
                posicaoYFlor = random.choice(linhas)
        if (retanguloPascal.colliderect(retanguloObstaculo1) and tempoInvulneravel == 0):
            vidas -= 1
            tempoInvulneravel = 60
            if linhaAtual == 0:
                linhaAtual += 1
            elif linhaAtual == 4:
                linhaAtual -= 1
            else:
                direcao = random.choice([-1,1])
                linhaAtual += direcao
        if (retanguloPascal.colliderect(retanguloObstaculo2) and tempoInvulneravel == 0):
            vidas -= 1
            tempoInvulneravel = 60
            if linhaAtual == 0:
                linhaAtual += 1
            elif linhaAtual == 4:
                linhaAtual -= 1
            else:
                direcao = random.choice([-1,1])
                linhaAtual += direcao
        if (retanguloPascal.colliderect(retanguloObstaculo3) and tempoInvulneravel == 0):
            vidas -= 1
            tempoInvulneravel = 60
            if linhaAtual == 0:
                linhaAtual += 1
            elif linhaAtual == 4:
                linhaAtual -= 1
            else:
                direcao = random.choice([-1,1])
                linhaAtual += direcao
        if vidas <= 0:
            game_over(nome, pontos)
            return
                            
        if pontos >= 5:
            velocidadeFundo = 4
        if pontos >= 12:
            velocidadeFundo = 5
        if pontos >= 20:
            velocidadeFundo = 6
        if pontos >= 30:
            velocidadeFundo = 7
        if pontos >= 42:
            velocidadeFundo = 8
        if pontos >= 55:
            velocidadeFundo = 9
        
        if crescendoSol:
            raioSol += 0.6
            if raioSol >= 50:
                crescendoSol = False
        else:
            raioSol -= 0.6
            if raioSol <= 20:
                crescendoSol = True

        contadorBorboleta += 1
        if contadorBorboleta >= 30:
            posicaoXBorboleta += random.randint(-20,20)
            posicaoYBorboleta += random.randint(-15,15)
            posicaoXBorboleta = max(0, min(posicaoXBorboleta, 950))
            posicaoYBorboleta = max(0, min(posicaoYBorboleta, 150))
            contadorBorboleta = 0
        fundoX1 -= velocidadeFundo
        fundoX2 -= velocidadeFundo
        posicaoXLanterna -= velocidadeFundo
        posicaoXObstaculo1 -= velocidadeFundo
        posicaoXObstaculo2 -= velocidadeFundo
        posicaoXObstaculo3 -= velocidadeFundo
        posicaoXFlor -= velocidadeFundo
        if fundoX1 <= -1000:
            fundoX1 = 1000
        if fundoX2 <= -1000:
            fundoX2 = 1000
        if posicaoXLanterna < -100:
            posicaoXLanterna = random.randint(1000,1500)
            posicaoYLanterna = random.choice(linhas)
            while ((posicaoYLanterna == posicaoYObstaculo1 and abs(posicaoXLanterna - posicaoXObstaculo1) < 250) or (posicaoYLanterna == posicaoYObstaculo2 and abs(posicaoXLanterna - posicaoXObstaculo2) < 250) or (posicaoYLanterna == posicaoYObstaculo3 and abs(posicaoXLanterna - posicaoXObstaculo3) < 250) or (posicaoYLanterna == posicaoYFlor and abs(posicaoXLanterna - posicaoXFlor) < 250)):
                posicaoXLanterna = random.randint(1000,1500)
                posicaoYLanterna = random.choice(linhas)
        if posicaoXObstaculo1 < -100:
            posicaoXObstaculo1 = random.randint(1000,1200)
            linhaObstaculo = random.choice(linhas)
            if random.randint(1,100) <= 75:
                while (linhaObstaculo == posicaoYObstaculo2 or linhaObstaculo == posicaoYObstaculo3):
                    linhaObstaculo = random.choice(linhas)
            while (linhaObstaculo == posicaoYLanterna or linhaObstaculo == posicaoYFlor):
                linhaObstaculo = random.choice(linhas)
            posicaoYObstaculo1 = linhaObstaculo
            obstaculoAtual1 = random.choice(listaObstaculos)
        if posicaoXObstaculo2 < -100:
            posicaoXObstaculo2 = random.randint(1150,1350)
            linhaObstaculo = random.choice(linhas)
            if random.randint(1,100) <= 75:
                while (linhaObstaculo == posicaoYObstaculo1 or linhaObstaculo == posicaoYObstaculo3):
                    linhaObstaculo = random.choice(linhas)
            while linhaObstaculo == posicaoYObstaculo1:
                linhaObstaculo = random.choice(linhas)
            while (linhaObstaculo == posicaoYLanterna or linhaObstaculo == posicaoYFlor):
                linhaObstaculo = random.choice(linhas)
            posicaoYObstaculo2 = linhaObstaculo
            obstaculoAtual2 = random.choice(listaObstaculos)
        if posicaoXObstaculo3 < -100:
            posicaoXObstaculo3 = random.randint(1300,1600)
            linhaObstaculo = random.choice(linhas)
            while (linhaObstaculo == posicaoYObstaculo1 or linhaObstaculo == posicaoYObstaculo2):
                    linhaObstaculo = random.choice(linhas)
            if random.randint(1,100) <= 75:
                while (linhaObstaculo == posicaoYObstaculo1 or linhaObstaculo == posicaoYObstaculo2):
                    linhaObstaculo = random.choice(linhas)
            while (linhaObstaculo == posicaoYLanterna or linhaObstaculo == posicaoYFlor):
                linhaObstaculo = random.choice(linhas)
            posicaoYObstaculo3 = linhaObstaculo
            obstaculoAtual3 = random.choice(listaObstaculos)
        if posicaoXFlor < -100:
            posicaoXFlor = random.randint(8000,15000)
            posicaoYFlor = random.choice(linhas)
            while ((posicaoYFlor == posicaoYObstaculo1 and abs(posicaoXFlor - posicaoXObstaculo1) < 250) or (posicaoYFlor == posicaoYObstaculo2 and abs(posicaoXFlor - posicaoXObstaculo2) < 250) or (posicaoYFlor == posicaoYObstaculo3 and abs(posicaoXFlor - posicaoXObstaculo3) < 250) or (posicaoYFlor == posicaoYLanterna and abs(posicaoXFlor - posicaoXLanterna) < 250)):
                posicaoXFlor = random.randint(8000,15000)
                posicaoYFlor = random.choice(linhas)

        tela.blit(fundo, (fundoX1,0))
        tela.blit(fundo, (fundoX2,0))
        sol_pulsante(tela, 970,30, int(raioSol))
        tela.blit(lanterna, (posicaoXLanterna, posicaoYLanterna))
        tela.blit(obstaculoAtual1, (posicaoXObstaculo1, posicaoYObstaculo1))
        tela.blit(obstaculoAtual2, (posicaoXObstaculo2, posicaoYObstaculo2))
        tela.blit(obstaculoAtual3, (posicaoXObstaculo3, posicaoYObstaculo3))
        tela.blit(flor, (posicaoXFlor, posicaoYFlor))
        if tempoInvulneravel == 0:
            tela.blit(pascal, (posicaoXPascal, posicaoYPascal))
        else:
            if tempoInvulneravel % 10 < 5:
                tela.blit(pascal, (posicaoXPascal, posicaoYPascal))
        tela.blit(borboleta, (posicaoXBorboleta,posicaoYBorboleta))
        textoPontos = fonteHUD.render(f"Pontos: {pontos}", True, branco)
        tela.blit(textoPontos, (20,660))
        tela.blit(coracao, (12,10))
        textoVida = fonteHUD.render(f"{vidas}", True, branco)
        tela.blit(textoVida, (33,18))
        textoPause = fonteHUD.render("Press Space to Pause Game", True, branco)
        tela.blit(textoPause, (745,660))

        pygame.display.update()
        relogio.tick(60)

while True:
    tela_inicio()
    jogo()