from island import Island
from searchAgents import *
from search import *
from graphics import Graphics

def manhattan(state, problem):
    gx, gy = problem.island.goal
    x, y = state
    return abs(x - gx) + abs(y - gy)

# Cargar isla
island = Island("island_map.txt")
problem = IslandSearchProblem(island)

# Elegir algoritmo
agent = SearchAgent(aStarSearch, heuristic=manhattan)
# agent = SearchAgent(breadthFirstSearch)
# agent = SearchAgent(uniformCostSearch)

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

# Animación
graphics = Graphics(island)
graphics.animate(positions, delay=0.6)
