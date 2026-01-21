from search import *

class IslandSearchProblem(SearchProblem):
    def __init__(self, island):
        self.island = island

    def getStartState(self):
        return self.island.start

    def isGoalState(self, state):
        return state == self.island.goal

    def getSuccessors(self, state):
        successors = []
        for action, (dx, dy) in self.island.actions.items():
            next_state = (state[0] + dx, state[1] + dy)
            if self.island.is_valid(next_state):
                cost = self.island.get_cost(next_state)
                successors.append((next_state, action, cost))
        return successors


class SearchAgent:
    def __init__(self, algorithm, heuristic=None):
        self.algorithm = algorithm
        self.heuristic = heuristic

    def plan(self, problem):
        if self.heuristic:
            return self.algorithm(problem, self.heuristic)
        return self.algorithm(problem)
