class Island:
    def __init__(self, map_file):
        self.map = []
        self.actions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        with open(map_file) as f:
            for i, line in enumerate(f):
                row = line.strip().split()
                for j, cell in enumerate(row):
                    if cell == "S":
                        self.start = (i, j)
                    elif cell == "T":
                        self.goal = (i, j)
                self.map.append(row)

    def is_valid(self, state):
        x, y = state
        if x < 0 or y < 0:
            return False
        if x >= len(self.map) or y >= len(self.map[0]):
            return False
        return self.map[x][y] != "#"

    def get_cost(self, state):
        x, y = state
        if self.map[x][y] == "~":
            return 2
        return 1
