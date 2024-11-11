import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Banana Kong Style")

# Definindo cores (apenas para objetos)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Definindo o clock para controlar o FPS
clock = pygame.time.Clock()

# Carregando a imagem de fundo
background_image = pygame.image.load('c:/Users/SENAI/Documents/jogo1.pnj.jfif')  # Substitua com o caminho correto da sua imagem
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Classe para o jogador (personagem)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Criando uma superfície para o personagem
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (40, screen_height - 50   )
        self.velocity_y = 0
        self.is_jumping = False
        print(self.rect.center)

    def update(self): 
        # Movimentação lateral
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Gravidade
        self.velocity_y += 1  # Aumenta a velocidade de queda
        self.rect.y += self.velocity_y

        # Pulo
        if self.rect.bottom >= screen_height - 20:  # Chão
            self.velocity_y = 0
            self.rect.bottom = screen_height - 20
            self.is_jumping = False
        elif self.rect.bottom < screen_height - 20:  # Se está no ar
            self.is_jumping = True

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -15  # Força do pulo


# Classe para os obstáculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = screen_height - 30

    def update(self):
        self.rect.x -= 5  # Movimento dos obstáculos
        if self.rect.right < 0:
            self.rect.x = screen_width
            self.rect.y = screen_height - 30  # Define uma nova posição vertical
            self.rect.height = random.randint(20, 50)  # Aleatoriza a altura dos obstáculos

# Função para desenhar o fundo
def draw_background():
    screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo na tela


# Função principal do jogo
def game_loop():
    # Grupo de todos os sprites
    all_sprites = pygame.sprite.Group()

    # Adicionando o personagem
    player = Player()
    all_sprites.add(player)

    # Adicionando obstáculos
    obstacles = pygame.sprite.Group()
    for _ in range(50):  # Adiciona 5 obstáculos no início
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Espaço para pular
                    player.jump()

        # Atualizar os sprites
        all_sprites.update()

        # Verificar colisão com obstáculos
        if pygame.sprite.spritecollide(player, obstacles, False):
            print("Game Over!")
            running = False

        # Desenhar o fundo e os sprites
        draw_background()
        all_sprites.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar o FPS
        clock.tick(60)

    pygame.quit()


# Iniciar o jogo
game_loop()
