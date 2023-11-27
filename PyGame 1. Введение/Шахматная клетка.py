import pygame

pygame.init()

inp = input().split()
size = (int(inp[0]), int(inp[0]))
screen = pygame.display.set_mode(size)
square_size = int(inp[0]) / int(inp[1])

pygame.display.set_caption("&&&&")

# rgb
white_color = (255, 255, 255)
black_color = (0, 0, 0)


def draw_squares(screen):
    screen.fill(white_color)
    for row in range(int(inp[0])):
        for col in range(row % 2, int(inp[0]), 2):
            pygame.draw.rect(screen, black_color, (col * square_size, row * square_size, square_size, square_size))


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

    draw_squares(screen)
    pygame.display.update()

pygame.quit()
