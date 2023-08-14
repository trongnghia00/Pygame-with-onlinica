import pygame

# Thiết lập màn hình
SCREEN_TITLE = 'My game'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Định nghĩa 2 màu cơ bản
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Class tổng quát dành cho các đối tượng trong game
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Vẽ đối tượng lên màn hình
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class Game:
    TICK_RATE = 60 # FPS

    # Hàm khởi tạo
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Thiết lập màn hình
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        # Thiết lập hình nền
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self):
        is_game_over = False

        # Khởi tạo đối tượng hộp kho báu
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        # Gameloop
        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

            # Vẽ lại màn hình
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            # Vẽ hộp kho báu
            treasure.draw(self.game_screen)

            # Update
            pygame.display.update()

            # Clock
            clock.tick(self.TICK_RATE)


# Chương trình chính
pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()