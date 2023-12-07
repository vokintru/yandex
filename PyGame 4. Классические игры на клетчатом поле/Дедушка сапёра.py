import pygame
import random
from board import Board


class Minesweeper(Board):
    def __init__(self, width, height, mine):
        super().__init__(width, height)
        self.mine = mine
        self.board = [[-1] * self.width for _ in range(self.height)]
        print(self.board)
        while self.mine:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            print()
            if self.board[y][x] != 10:
                self.board[y][x] = 10
                self.mine -= 1

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color(0, 255, 0),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                if 0 <= self.board[y][x] <= 8:
                    font = pygame.font.Font(None, 25)
                    text = font.render(f"{self.board[y][x]}", True, (100, 255, 100))
                    screen.blit(text, (x * self.cell_size + self.left, y * self.cell_size + self.top))

                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def open_cell(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        s = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                    continue
                if self.board[y + dy][x + dx] == 10:
                    s += self.board[y + dy][x + dx]
        self.board[y][x] = s // 10


    def on_click(self, cell):
        print(cell)
        self.open_cell(cell)


def main():
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дедушка сапёра')
    clock = pygame.time.Clock()
    board = Minesweeper(10, 15, 10)
    ticks = 0
    running = True
    FPS = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
        ticks += 1
    pygame.quit()


if __name__ == '__main__':
    main()
