from function_commands import *
from heuristic_commands import *
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute() -> None:
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


class Compare:
    @staticmethod
    def a_star_ida_star_compare(x: int, y: int):
        function = Function()
        manhattan_distance_command_function_x = ManhattanDistanceCommandFunctionCommand(function, x)
        manhattan_distance_command_function_y = ManhattanDistanceCommandFunctionCommand(function, y)
        invoker = Invoker()
        invoker.register(manhattan_distance_command_function_x, "manhattan_distance_command_function_x")
        invoker.register(manhattan_distance_command_function_y, "manhattan_distance_command_function_y")
        return invoker.execute("manhattan_distance_command_function_x") \
            - invoker.execute("manhattan_distance_command_function_y")

    @staticmethod
    def greedy_compare(x: int, y: int):
        heuristic = Heuristic()
        manhattan_distance_heuristic_x = ManhattanDistanceCommand(heuristic, x.state)
        manhattan_distance_heuristic_y = ManhattanDistanceCommand(heuristic, y.state)
        invoker = Invoker()
        invoker.register(manhattan_distance_heuristic_x, "manhattan_distance_heuristic_x")
        invoker.register(manhattan_distance_heuristic_y, "manhattan_distance_heuristic_y")

        result = invoker.execute("manhattan_distance_heuristic_x") \
                 - invoker.execute("manhattan_distance_heuristic_y")

        if result > 0:
            return 1
        elif result == 0:
            return 0

        return -1

class AStarIDAStarCompareCommand(Command):
    def __init__(self, compare, x, y):
        self.__compare = compare
        self.x = x
        self.y = y

    def execute(self):
        self.__compare.a_star_ida_star_compare(self.x, self.y)

class GreedyCompareCommand(Command):
    def __init__(self, compare, x, y):
        self.__compare = compare
        self.x = x
        self.y = y

    def execute(self):
        self.__compare.greedy_compare_command(self.x, self.y)
