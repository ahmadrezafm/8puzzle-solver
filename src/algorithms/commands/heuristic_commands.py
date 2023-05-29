from abc import ABCMeta, abstractmethod


class Command(ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


class Invoker:
    def __init__(self):
        self.__commands = {}

    def register(self, command, command_name):
        self.__commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.__commands.keys():
            self.__commands[command_name].execute()

        else:
            print(f"not recognized command")


class Heuristic:
    @staticmethod
    def out_place_tiles(state, goal):
        cost = 0

        def increment(cost: int) -> int:
            return cost + 1

        [state[i] != goal[i] and increment(cost) for i in range(len(state))]

        # for i in range(len(state)):
        #     if state[i] != goal[i]:
        #         cost += 1

        return cost

    @staticmethod
    def manhattan_distance(state):
        def board_state(state):
            i = 0
            temp = [([0] * 3) for j in range(3)]
            for row in range(3):
                for col in range(3):
                    temp[row][col] = state[i]
                    i += 1
            return temp

        final_position = [(1, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
        cost = 0
        temp = board_state(state=state)
        for y in range(3):
            for x in range(3):
                t = temp[x][y]
                xf, yf = final_position[t]
                cost += abs(xf - x) + abs(yf - y)

        return cost

class OutPlaceTilesCommand(Command):
    def __init__(self, heuristic, state, goal):
        self.__heuristic = heuristic
        self.state = state
        self.goal = goal

    def execute(self):
        self.__heuristic.out_place_tiles(self.state, self.goal)

class ManhattanDistanceCommand(Command):
    def __init__(self, heuristic, state):
        self.__heuristic = heuristic
        self.state = state

    def execute(self):
        self.__heuristic.manhattan_distance(self.state)
