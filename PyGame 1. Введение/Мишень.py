import pygame

pygame.init()

n, k = [int(i) for i in input().split()]
a = n * k * 2
h = n * k
screen = pygame.display.set_mode((a, a))
pygame.display.set_caption('first')
color = ['#0000ff', '#00ff00', '#ff0000']

def draw(h):
#k % 3 == 0: y
# k % 3 == 1: y + 2
# k % 3 == 2: y + 1
    for y in range(k):
        pygame.draw.circle(screen, pygame.Color(color[(y - k) % 3]), (a // 2, a // 2), h)
        h -= n


draw(h)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.flip()

pygame.quit()