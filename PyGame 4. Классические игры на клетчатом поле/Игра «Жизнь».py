import pygame
import copy
from board import Board


class Life(Board):
    # создание поля
    def init(self, width, height):
        super().init(width, height)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    pygame.draw.rect(screen, pygame.Color(0, 255, 0),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        print(cell)
        self.board[cell[1]][cell[0]] = 1

    def next_move(self):
        # сохраняем поле
        tmp_board = copy.deepcopy(self.board)
        # пересчитываем
        for y in range(self.height):
            for x in range(self.width):
                # сумма окружающих клеток
                s = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                            continue
                        s += self.board[y + dy][x + dx]
                s -= self.board[y][x]
                if s == 3:
                    tmp_board[y][x] = 1
                elif s < 2 or s > 3:
                    tmp_board[y][x] = 0
        # обновляем поле
        self.board = copy.deepcopy(tmp_board)


def main():
    pygame.init()
    size = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 40

    board = Life(25, 25)
    board.set_view(1, 1, 20)

    running = True
    living = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if living:
                    living = False
                else:
                    living = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                FPS += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                FPS -= 1
        if living:
            board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
