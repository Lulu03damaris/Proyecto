import pygame
import time

CELL_SIZE = 40

class Graphics:
    def __init__(self, island):
        pygame.init()
        self.island = island
        self.screen = pygame.display.set_mode(
            (len(island.map[0]) * CELL_SIZE,
             len(island.map) * CELL_SIZE)
        )
        pygame.display.set_caption("Agente en Busca del Tesoro")

    def draw_map(self):
        colors = {
            "#": (0, 0, 0),        # Obstáculo
            ".": (255, 255, 255),  # Terreno
            "~": (180, 180, 180),  # Agua
            "S": (0, 255, 0),      # Inicio
            "T": (255, 215, 0)     # Tesoro
        }

        for i, row in enumerate(self.island.map):
            for j, cell in enumerate(row):
                color = colors.get(cell, (255, 255, 255))
                pygame.draw.rect(
                    self.screen,
                    color,
                    (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    def draw_agent(self, position):
        x, y = position
        pygame.draw.circle(
            self.screen,
            (0, 0, 255),
            (y * CELL_SIZE + CELL_SIZE // 2,
             x * CELL_SIZE + CELL_SIZE // 2),
            CELL_SIZE // 3
        )

    def animate(self, positions, delay=0.5):
        for pos in positions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.fill((0, 0, 0))
            self.draw_map()
            self.draw_agent(pos)
            pygame.display.flip()
            time.sleep(delay)
