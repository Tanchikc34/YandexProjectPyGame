import pygame
import sys
from settings import *
from level import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("World of Lost Souls")
        self.clok = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("white")
            self.level.run()
            pygame.display.update()
            self.clok.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
