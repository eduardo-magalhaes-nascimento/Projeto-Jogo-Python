import pygame, random

pygame.init()

janela = pygame.display.set_mode([960, 540])
pygame.display.set_caption('Nave 2.0')
fps = pygame.time.Clock()

# FUNDO DO  GAME
bg = pygame.image.load('C:/Programas py/jogos/jogo 2/imagem/space bg game.png')

# IMAGEM DO JOGADOR
jogador = pygame.image.load('C:/Programas py/jogos/jogo 2/imagem/sprite_nave_pequena.png')

# IMAGEM DO INIMIGO
inimigo = pygame.image.load('C:/Programas py/jogos/jogo 2/imagem/nave_inimiga_pequena.png')
inimigo = pygame.transform.scale(inimigo, (80, 64))

# IMAGEM DO PROJETIL
missil = pygame.image.load('C:/Programas py/jogos/jogo 2/imagem/missil_pequeno.png')
missil = pygame.transform.scale(missil, (40, 40))



# POSIÇÕES JOGADOR:
pos_jog_y = 420
pos_jog_x = 430
vel_jog = 10

# POSIÇÕES INIMIGO:
pos_inim_x = 430
pos_inim_y = 30
vel_inim = 5

# POSIÇÃO DO MISSIL
pos_missil_x = pos_jog_x + 27
pos_missil_y = pos_jog_y
vel_missil = 10
tiro = False

pontuacao = 0
game_over = False
def colisoes():
    global pos_inim_x
    global pos_inim_y
    global pontuacao
    global game_over

    if jogador_rect.colliderect(inimigo_rect):
        game_over = True
    
    elif inimigo_rect.y > 510:
        pontuacao -= 1
        return True
    
    elif missil_rect.colliderect(inimigo_rect):
        pos_inim_y = -1200
        pontuacao += 1
        if pos_inim_y < -1000:
            aleatoria_x = random.randint(1, 870)
            pos_inim_x = aleatoria_x
            pos_inim_y = -90


def resultado():
    if pontuacao > 0:
        print(f'VOCÊ GANHOU FAZENDO {pontuacao} pontos')
    else:
        print(f'GAME OVER FAZENDO {pontuacao} pontos')

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if game_over:
        loop = False

#  MOVIMENTO INIMIGO 
    pos_inim_y += vel_inim
    if pos_inim_y == 520:
        aleatoria_x =  random.randint(1, 870)
        pos_inim_y = 0
        pos_inim_x = aleatoria_x
        


# MOVIMENTO JOGADOOR
    tecla = pygame.key.get_pressed()
    # Jogador se move para cima e não passa da posição -5
    if pos_jog_y > -5:
        if tecla[pygame.K_UP]:
            pos_jog_y -= vel_jog

    # Jogador se move para baixo e não passa da posição 460
    if pos_jog_y < 460:
        if tecla[pygame.K_DOWN]:
            pos_jog_y += vel_jog

    # Jogador se move para esquerda e não passa da posição 0
    if pos_jog_x > 0:
        if tecla[pygame.K_LEFT]:
            pos_jog_x -= vel_jog

    # Jogador se move para direita e não passa da posição 865
    if pos_jog_x < 865:
        if tecla[pygame.K_RIGHT]:
            pos_jog_x += vel_jog



# Botão do missel
    if tecla[pygame.K_SPACE]:
        tiro = True
        if tiro:
            pos_missil_x = pos_jog_x
            pos_missil_y -= vel_missil
            if pos_missil_y < 1:
                tiro =True
                pos_missil_y = pos_jog_y
                pos_missil_x = pos_jog_x

    if tiro:
        pos_missil_y -= vel_missil

    jogador_rect = jogador.get_rect()
    inimigo_rect = inimigo.get_rect()
    missil_rect  = missil.get_rect()

    jogador_rect.x = pos_jog_x
    jogador_rect.y = pos_jog_y

    inimigo_rect.x = pos_inim_x
    inimigo_rect.y =pos_inim_y

    missil_rect.x = pos_missil_x
    missil_rect.y = pos_missil_y

    
    janela.blit(bg, (0,0))
    janela.blit(inimigo, (pos_inim_x, pos_inim_y))
    janela.blit(missil, (pos_missil_x, pos_missil_y))
    janela.blit(jogador,(pos_jog_x, pos_jog_y))



    '''pygame.draw.rect(janela, (255,0,0), jogador_rect,2)
    pygame.draw.rect(janela, (255,0,0), inimigo_rect,2)
    pygame.draw.rect(janela, (255,0,0), missil_rect,2)'''


    colisoes()
    fps.tick(60)
    pygame.display.update()

print('='*10)
resultado()
print('='*10)