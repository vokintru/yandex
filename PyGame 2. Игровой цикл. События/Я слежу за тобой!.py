import pygame

pygame.init()
pygame.display.set_caption('Я слежу за тобой')
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
running = True
count = 1
color = pygame.Color("red")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.WINDOWHIDDEN:
            count += 1
        if event.type == pygame.WINDOWSHOWN:
            font = pygame.font.Font(None, 100)
            text = font.render(str(count), True, color)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            print(count)
    pygame.display.flip()
pygame.quit()
