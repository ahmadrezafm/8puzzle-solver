from heuristic_commands import *
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

class Function:
    @staticmethod
    def out_place_tile_command_function(node):
        heuristic = Heuristic()
        out_place_tile_heuristic = OutPlaceTilesCommand(heuristic, node.state, [1, 2, 3, 8, 0, 4, 7, 6, 5])
        invoker = Invoker()
        invoker.register(out_place_tile_heuristic, "out_place_tile_heuristic")
        return node.depth + invoker.execute("out_place_tile_heuristic")

    @staticmethod
    def manhattan_distance_command_function(node):
        heuristic = Heuristic()
        manhattan_distance_heuristic = ManhattanDistanceCommand(heuristic, node.state)
        invoker = Invoker()
        invoker.register(manhattan_distance_heuristic, "manhattan_distance_heuristic")
        return node.depth + invoker.execute("manhattan_distance_heuristic")

class out_place_tile_command_function_command(Command):
    def __init__(self, function, node):
        self.__function = function
        self.node = node

    def execute(self):
        self.__function.out_place_tile_command_function(self.node)

class manhattan_distance_command_function_command(Command):
    def __init__(self, function, node):
        self.__function = function
        self.node = node

    def execute(self):
        self.__function.manhattan_distance_command_function(self.node)
