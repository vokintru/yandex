import pygame
import random
from board import Board


class Minesweeper(Board):
    def __init__(self, width, height, need):
        super().__init__(width, height)
        self.board = [[-1] * width for inet in range(height)]
        ter = 0
        while ter < need:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == -1:
                self.board[y][x] = 10
                ter += 1

    def open_click(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        s = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                    continue
                if self.board[y + dy][x + dx] == 10:
                    s += 1
        if s == 0:
            s1 = 0
            for x1 in range(self.width):
                for y1 in range(self.height):
                    s1 = 0
                    if self.board[y1][x1] == -1:
                        for dy1 in range(-1, 2):
                            for dx1 in range(-1, 2):
                                if x1 + dx1 < 0 or x1 + dx1 >= self.width or y1 + dy1 < 0 or y1 + dy1 >= self.height:
                                    continue
                                if self.board[y1 + dy1][x1 + dx1] == 10:
                                    s1 += 1
                        if s1 == 0:
                            self.board[y1][x1] = s1
        self.board[y][x] = s

    def on_click(self, cell):
        self.open_click(cell)

    def render(self, screen):
        color = pygame.Color('red')
        for y in range(self.height):
            for x in range(self.width):
                coor = (x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size)
                coor1 = (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2,
                         self.cell_size, self.cell_size)
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, color, coor)
                pygame.draw.rect(screen, pygame.Color('white'), coor, 1)
                if self.board[y][x] >= 0 and self.board[y][x] != 10:
                    font = pygame.font.Font(None, self.cell_size - 7)
                    text = font.render(str(self.board[y][x]), 1, (100, 255, 100))
                    screen.blit(text, coor1)


def main():
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Папа сапёра')
    clock = pygame.time.Clock()
    board = Minesweeper(10, 15, 10)
    ticks = 0
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
        clock.tick(50)
        ticks += 1
    pygame.quit()


if __name__ == '__main__':
    main()