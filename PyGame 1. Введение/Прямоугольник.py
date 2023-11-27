import pygame

x, y = map(int, input().split())
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('&&&&&&&')


def draw():
    pygame.draw.rect(screen, pygame.Color('#ff0000'), (1, 1, x - 2, y - 2))


draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()


pygame.quit()
