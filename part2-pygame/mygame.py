import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ đồ họa
width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

#Thay đổi màu nền cửa sổ
background_color = (255, 255, 255)
screen.fill(background_color)
pygame.display.update()

# Thiết lập thời gian
clock = pygame.time.Clock()

# Màu đường vẽ
line_color = (random.randint(0,255), 0, 0)

# Số lượng đường thẳng ngẫu nhiên
num = 2

# Vòng lặp chính của ứng dụng
running = True
while running:
    clock.tick(60)  # Giới hạn 60 lần lặp mỗi giây

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Thiết lập màu vẽ
    color = (random.randint(0,255), 0, 0)

    # Vẽ nhiều đường tròn ngẫu nhiên
    for _ in range(num):
        center = (random.randint(0, width), random.randint(0, height))
        radius = random.randint(10, 50)
        pygame.draw.circle(screen, color, center, radius)

    # Cập nhật trạng thái của trò chơi (nhân vật, điểm số, các sự kiện, các hình ảnh, ...)
    pygame.display.update()

# Kết thúc Pygame
pygame.quit()