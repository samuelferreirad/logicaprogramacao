import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Banana Kong Style")

# Definindo o clock para controlar o FPS
clock = pygame.time.Clock()

# Carregando as imagens
background_image = pygame.image.load('c:/Users/SENAI/Pictures/hsdghsf.png')  # Substitua com o caminho correto da sua imagem
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

player_image = pygame.image.load('c:/Users/SENAI/Pictures/boneca.png')  # Substitua com o caminho correto da sua imagem do jogador
player_image = pygame.transform.scale(player_image, (150, 150))  # Ajuste o tamanho da imagem do jogador conforme necessário

# Classe para o jogador (personagem)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 3, screen_height - self.rect.height // 2)
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_jumping = False
        self.speed = 5

    def update(self):
        # Impede o jogador de sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        # Pulo do jogador
        if self.is_jumping:
            self.velocity_y += 1  # Gravidade
            self.rect.y += self.velocity_y

            if self.rect.bottom > screen_height - 50:
                self.rect.bottom = screen_height - 50
                self.is_jumping = False
                self.velocity_y = 0

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -15
            self.is_jumping = True


# Função para desenhar o fundo
def draw_background(background_x):
    screen.blit(background_image, (background_x % screen_width - screen_width, 0))
    screen.blit(background_image, (background_x % screen_width, 0))


# Função para desenhar a tela de início
def draw_start_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("Pressione qualquer tecla para começar", True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    pygame.display.update()


# Função principal do jogo
def game_loop():
    all_sprites = pygame.sprite.Group()

    # Adicionando o jogador
    player = Player()
    all_sprites.add(player)

    background_x = 0
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

        # Atualizar a posição do fundo
        background_x -= 5

        # Desenhar o fundo e os sprites
        draw_background(background_x)
        all_sprites.draw(screen)

        # Atualizar a tela
        pygame.display.update()

        # Controlar o FPS
        clock.tick(60)

    pygame.quit()


# Função para iniciar o jogo e mostrar a tela inicial
def start_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Iniciar o jogo ao pressionar qualquer tecla
                    game_loop()

        # Desenhar a tela de início
        draw_start_screen()

        # Controlar o FPS
        clock.tick(30)

    pygame.quit()


# Iniciar o jogo com a tela de início
start_screen()
