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

# Khởi tạo font
pygame.font.init()
font = pygame.font.SysFont('Arial', 75)

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

# Class cho nhân vật game
class PlayerCharacter(GameObject):
    # Tốc độ di chuyển
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Hàm cho phép nhân vật di chuyển, direction > 0 => đi lên, ngược lại đi xuống
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        # Đảm bảo nhân vật không di chuyển vượt khỏi màn hình bên dưới
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    # Hàm kiểm tra va chạm, trả về True nếu có va chạm
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        
        return True

# Class cho NPC (các enemy)
class NonPlayerCharacter(GameObject):
    # Tốc độ enemy
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 0:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


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
        direction = 0

        # Khởi tạo đối tượng hộp kho báu
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        # Khởi tạo nhân vật
        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)

        # Khởi tạo enemy
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 50, 50)
        enemy_1 = NonPlayerCharacter('enemy.png', self.width - 40, 400, 50, 50)
        enemy_2 = NonPlayerCharacter('enemy.png', 400, 200, 50, 50)

        # Gameloop
        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Sự kiện xảy ra khi có nút được nhấn xuống
                elif event.type == pygame.KEYDOWN:
                    # Nút nhấn là mũi tên lên
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Nút nhấn là mũi tên xuống
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Sự kiện xảy ra khi không còn nhấn nút
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                # print(event)

            # Vẽ lại màn hình
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            # Vẽ hộp kho báu
            treasure.draw(self.game_screen)

            # Cập nhật vị trí của nhân vật sau di chuyển
            player_character.move(direction, self.height)
            # Vẽ nhân vật ra màn hình
            player_character.draw(self.game_screen)

            # Cập nhật vị trí và vẽ enemy
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            enemy_1.move(self.width)
            enemy_1.draw(self.game_screen)

            enemy_2.move(self.width)
            enemy_2.draw(self.game_screen)

            # Kiểm tra thắng thua và hiển thị thông báo
            if player_character.detect_collision(enemy_0) or player_character.detect_collision(enemy_1) or player_character.detect_collision(enemy_2):
                is_game_over = True
                text = font.render('Game Over :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                pygame.time.delay(2000)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                text = font.render('You win! :)', True, BLACK_COLOR)
                self.game_screen.blit(text, (225, 350))
                pygame.display.update()
                pygame.time.delay(2000)
                break

            # Update
            pygame.display.update()

            # Clock
            clock.tick(self.TICK_RATE)


# Chương trình chính
pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()