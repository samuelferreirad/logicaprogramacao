import pygame

# Inicializando Pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True

# Carregando a imagem do jogador
player_image = pygame.image.load("C:\\Users\\SENAI\\Downloads\\ninja.png")  # Caminho atualizado
player_image = pygame.transform.scale(player_image, (80, 80))  # Ajustando o tamanho da imagem

player_pos = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)
player_2 = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Desenhar a imagem do jogador
    screen.blit(player_image, player_pos)
    pygame.draw.circle(screen, "white", player_2, 35)

    # Movimento do jogador 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 9
    if keys[pygame.K_s]:
        player_pos.y += 9
    if keys[pygame.K_a]:
        player_pos.x -= 9
    if keys[pygame.K_d]:
        player_pos.x += 9

    # Limites do jogador 1
    
    player_pos.x = max(3, min(player_pos.x, 720))
    player_pos.y = max(0, min(player_pos.y, 420))

    # Movimento do jogador 2
    if keys[pygame.K_UP]:
        player_2.y -= 9
    if keys[pygame.K_DOWN]:
        player_2.y += 9
    if keys[pygame.K_LEFT]:
        player_2.x -= 9
    if keys[pygame.K_RIGHT]:
        player_2.x += 9

    # Limites do jogador 2
    player_2.x = max(43, min(player_2.x, 760))
    player_2.y = max(41, min(player_2.y, 455))

    # Atualizando a tela
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
