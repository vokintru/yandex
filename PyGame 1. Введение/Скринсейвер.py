import random
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('first')

x = 960
y = 540


def draw(x, y):
    pygame.draw.rect(screen, pygame.Color('#ffcc00'), (x, y, 100, 100))


draw(x, y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += random.randint(-4, 4)
    y += random.randint(-4, 4)
    pygame.draw.rect(screen, pygame.Color('#000000'), (0, 0, 0, 0))
    draw(x, y)
    pygame.display.flip()

pygame.quit()
