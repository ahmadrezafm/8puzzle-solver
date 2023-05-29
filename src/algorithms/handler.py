from a_star import *

class Solve:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def a_star(self):
        return perform_a_star(self.start, self.goal)

    def bfs(self):
        pass
