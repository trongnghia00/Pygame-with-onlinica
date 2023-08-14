import pygame

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

# Vòng lặp chính của ứng dụng
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Kết thúc Pygame
pygame.quit()