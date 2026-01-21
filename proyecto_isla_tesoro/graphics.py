import pygame

CELL_SIZE = 40

class Graphics:
    def __init__(self, island):
        pygame.init()
        self.island = island
        self.screen = pygame.display.set_mode(
            (len(island.map[0]) * CELL_SIZE,
             len(island.map) * CELL_SIZE)
        )

    def draw(self, path=None):
        colors = {
            "#": (0, 0, 0),
            ".": (255, 255, 255),
            "~": (180, 180, 180),
            "S": (0, 255, 0),
            "T": (255, 215, 0)
        }

        for i, row in enumerate(self.island.map):
            for j, cell in enumerate(row):
                color = colors.get(cell, (255, 255, 255))
                pygame.draw.rect(
                    self.screen,
                    color,
                    (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

        if path:
            for x, y in path:
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

        pygame.display.flip()
