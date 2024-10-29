import pygame


pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)
player_2 = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)
player_image = pygame.image.load("C:\\Users\\SENAI\\Downloads\\ninja.png")
player_image = pygame.transform.scale(player_image, (70, 70))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
 
    pygame.draw.circle(screen, "red", player_pos, 35)
    pygame.draw.circle(screen, "white", player_2, 35)
   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 9
    if keys[pygame.K_s]:
        player_pos.y += 9
    if keys[pygame.K_a]:
        player_pos.x -= 9
    if keys[pygame.K_d]:
        player_pos.x += 9
    if(player_pos==player_pos):
        print(player_pos)
    if player_pos.x>=760:
        player_pos.x=760
    if player_pos.x<=43:
        player_pos.x=43
    if player_pos.y<=41:
        player_pos.y=41
    if player_pos.y>=455:
        player_pos.y=455

#colisao player 2 

    if player_2.x>=755:
        player_2.x=755
    if player_2.x<=43:
        player_2.x=43
    if player_2.y>=455:
        player_2.y=455
    if player_2.y<=40:
        player_2.y=40
        keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_2.y -= 9
    if keys[pygame.K_DOWN]:
        player_2.y += 9
    if keys[pygame.K_LEFT]:
        player_2.x -= 9 
    if keys[pygame.K_RIGHT]:
        player_2.x += 9
    if(player_2==player_2):

        pygame.display.flip()

    dt = clock.tick(120) / 500

pygame.quit()