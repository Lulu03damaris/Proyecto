from island import Island
from searchAgents import *
from search import *
from graphics import Graphics
import time

def manhattan(state, problem):
    gx, gy = problem.island.goal
    x, y = state
    return abs(x - gx) + abs(y - gy)

island = Island("island_map.txt")
problem = IslandSearchProblem(island)

agent = SearchAgent(aStarSearch, heuristic=manhattan)
actions = agent.plan(problem)

# Convertir acciones en posiciones
positions = []
x, y = island.start
positions.append((x, y))

for action in actions:
    dx, dy = island.actions[action]
    x += dx
    y += dy
    positions.append((x, y))

graphics = Graphics(island)
graphics.draw(positions)


time.sleep(60)
