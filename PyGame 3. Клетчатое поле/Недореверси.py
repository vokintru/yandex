import random

import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        radius = 50
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
                if self.board[y][x]:
                    self.image = pygame.Surface((2 * radius, 2 * radius),
                                                pygame.SRCALPHA, 32)
                    pygame.draw.circle(self.image, pygame.Color("red"),
                                       (radius, radius), radius)
                else:
                    self.image = pygame.Surface((2 * radius, 2 * radius),
                                                pygame.SRCALPHA, 32)
                    pygame.draw.circle(self.image, pygame.Color("blue"),
                                       (radius, radius), radius)

                    # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x_click, y_click = mouse_pos
        x_cell = (x_click - self.left) // self.cell_size
        y_cell = (y_click - self.top) // self.cell_size
        if x_cell < 0 or x_cell >= self.width or y_cell < 0 or y_cell >= self.height:
            return None
        return x_cell, y_cell

    def on_click(self, cell):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if cell is None:
                    pass
                elif cell[0] == x:
                    if self.board[y][x] == 1:
                        self.board[y][x] = 0
                    else:
                        self.board[y][x] = 1
                elif cell[1] == y:
                    if self.board[y][x] == 1:
                        self.board[y][x] = 0
                    else:
                        self.board[y][x] = 1

    def update(self, x, y, z):
        self.board[y][x] = z


def main():
    pygame.init()
    size = 1920, 1080
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Недореверси')

    # поле 5 на 7
    # pole = input()
    pole = 20
    if int(pole) > 21:
        print("Поле не влезает на экран")
        exit()

    board = Board(int(pole), int(pole))
    board.set_view(500, 0, 50)

    for x in range(int(pole)):
        for y in range(int(pole)):
            board.update(x, y, random.randint(0, 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
