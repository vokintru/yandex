import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
FPS = 100
clock = pygame.time.Clock()


def game(cord):
    img = pygame.image.load('data/gameover.png')
    screen.fill((0, 0, 255))
    screen.blit(img, (cord, 0))

    pygame.display.flip()


if __name__ == '__main__':
    running = True
    cord = -600
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if cord < 2:
            game(cord)
            cord += 2

        clock.tick(FPS)
    pygame.quit()
