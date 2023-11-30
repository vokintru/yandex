import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('circles')
FPS = 100  # число кадров в секунду
clock = pygame.time.Clock()
circles = []
speed_x = []
speed_y = []
radius = 0


def draw(pos, r):
    pygame.draw.circle(screen, (255, 255, 0), pos, r)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            circles.append(event.pos)
            speed_x.append(1)
            speed_y.append(1)
            radius = 10
            draw(event.pos, radius)

    screen.fill((0, 0, 0))
    for i in range(len(circles)):
        pos_circle = circles[i]
        if pos_circle[0] >= 400 or pos_circle[0] <= 0:
            speed_x[i] = - speed_x[i]
        if pos_circle[1] >= 500 or pos_circle[1] <= 0:
            speed_y[i] = - speed_y[i]
        circles[i] = pos_circle[0] - speed_x[i], pos_circle[1] - speed_y[i]
        draw(circles[i], radius)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
