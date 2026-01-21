from collections import deque
import heapq

class SearchProblem:
    def getStartState(self):
        raise NotImplementedError

    def isGoalState(self, state):
        raise NotImplementedError

    def getSuccessors(self, state):
        """
        Retorna: (successor, action, cost)
        """
        raise NotImplementedError


def depthFirstSearch(problem):
    stack = [(problem.getStartState(), [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for succ, action, _ in problem.getSuccessors(state):
            stack.append((succ, path + [action]))

    return []


def breadthFirstSearch(problem):
    queue = deque([(problem.getStartState(), [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for succ, action, _ in problem.getSuccessors(state):
            queue.append((succ, path + [action]))

    return []


def uniformCostSearch(problem):
    pq = []
    heapq.heappush(pq, (0, problem.getStartState(), []))
    visited = {}

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        if problem.isGoalState(state):
            return path

        for succ, action, step_cost in problem.getSuccessors(state):
            heapq.heappush(pq, (cost + step_cost, succ, path + [action]))

    return []


def aStarSearch(problem, heuristic):
    pq = []
    heapq.heappush(pq, (0, 0, problem.getStartState(), []))
    visited = {}

    while pq:
        _, cost, state, path = heapq.heappop(pq)

        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        if problem.isGoalState(state):
            return path

        for succ, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            priority = new_cost + heuristic(succ, problem)
            heapq.heappush(pq, (priority, new_cost, succ, path + [action]))

    return []
