import pygame
from board import Board


class Lines(Board):
    # создание поля
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, pygame.Color(0, 0, 255),
                                     (x * self.cell_size + self.left + self.cell_size // 2,
                                      y * self.cell_size + self.top + self.cell_size // 2),
                                      self.cell_size // 2)
                if self.board[y][x] == 2:
                    pygame.draw.circle(screen, pygame.Color(255, 0, 0),
                                     (x * self.cell_size + self.left + self.cell_size // 2,
                                      y * self.cell_size + self.top + self.cell_size // 2),
                                      self.cell_size // 2)
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        print(cell)
        if self.board[cell[1]][cell[0]] % 2 == 0:
            self.board[cell[1]][cell[0]] = 1
        else:
            self.board[cell[1]][cell[0]] = 2


def main():
    pygame.init()
    size = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60

    board = Lines(5, 5)
    board.set_view(1, 1, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()