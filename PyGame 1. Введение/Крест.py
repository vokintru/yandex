import pygame


per = input().split()
feck_1 = int(per[0])
feck_2 = int(per[1])
pygame.init()
screen = pygame.display.set_mode((feck_1, feck_2))
pygame.display.set_caption('first')



def draw():
    pygame.draw.line(screen, pygame.Color('#FFFFFF'), (0, 0), (feck_1, feck_2), 5)
    pygame.draw.line(screen, pygame.Color('#FFFFFF'), (feck_1, 0), (0, feck_2), 5)

draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
