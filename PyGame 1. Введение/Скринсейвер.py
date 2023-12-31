import random
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('&&&&&&&&&&')

x = 960
y = 540

radius = random.randint(10, 50)
speed = radius - 5


def draw(x, y, hexadecimal):
    pygame.draw.circle(screen, pygame.Color(hexadecimal), (x, y), radius)


draw(x, y, "#ffffff")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += random.randint(-speed, speed)
    y += random.randint(-speed, speed)
    if x <= 0:
        x = 0
    if x >= 1920:
        x = 1920
    if y <= 0:
        y = 0
    if y >= 1080:
        y = 1080
    pygame.draw.rect(screen, pygame.Color('#000000'), (0, 0, 0, 0))
    #hexadecimal = ["#ff0000"]
    hexadecimal = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    draw(x, y, hexadecimal[0])
    pygame.display.flip()

pygame.quit()
