import pygame

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Banana Kong Style")

# Definindo o clock para controlar o FPS
clock = pygame.time.Clock()

# Carregando a imagem de fundo
background_image = pygame.image.load('c:/Users/SENAI/Pictures/imagemdofazen.png')  # Substitua com o caminho correto da sua imagem
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Carregando a imagem do jogador
player_image = pygame.image.load('c:/Users/SENAI/Pictures/cara.png')  # Substitua com o caminho correto da sua imagem do jogador
player_image = pygame.transform.scale(player_image, (100, 100))  # Ajuste o tamanho da imagem do jogador conforme necessário


# Classe para o jogador (personagem)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Atribuindo a imagem carregada ao jogador
        self.rect = self.image.get_rect()  # Obtendo o retângulo da imagem para posicionamento
        self.rect.center = (screen_width // 2, screen_height // 2)  # Centralizando o jogador na tela
        self.velocity_y = 0
        self.is_jumping = False

    def update(self): 
        # O jogador não se move lateralmente, então esse método permanece vazio para não alterar a posição dele
        pass

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -15  # Força do pulo


# Função para desenhar o fundo
def draw_background(background_x):
    # Desenha o fundo movendo-o para a esquerda
    screen.blit(background_image, (background_x % screen_width - screen_width, 0))  # Parte do fundo à esquerda
    screen.blit(background_image, (background_x % screen_width, 0))  # Parte do fundo à direita


# Função principal do jogo
def game_loop():
    # Grupo de todos os sprites
    all_sprites = pygame.sprite.Group()

    # Adicionando o personagem
    player = Player()
    all_sprites.add(player)

    # Inicializa a posição do fundo
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

        # Atualizar a posição do fundo, movendo-o para a esquerda
        background_x -= 5  # Move o fundo para a esquerda (ajuste conforme necessário)

        # Desenhar o fundo e os sprites (o jogador está parado)
        draw_background(background_x)
        all_sprites.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar o FPS
        clock.tick(60)

    pygame.quit()


# Iniciar o jogo
game_loop()
