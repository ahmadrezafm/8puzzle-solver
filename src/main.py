import random
import time


def display(state: list) -> None:
    print("-------------")
    print("| %i | %i | %i |" % (state[0], state[1], state[2]))
    print("-------------")
    print("| %i | %i | %i |" % (state[3], state[4], state[5]))
    print("-------------")
    print("| %i | %i | %i |" % (state[6], state[7], state[8]))
    print("-------------")


class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.__state = state
        self.__parent = parent
        self.__operator = operator
        self.__depth = depth
        self.__cost = cost

    def get_state(self):
        return self.__state

    def get_parent(self):
        return self.__parent

    def get_operator(self):
        return self.__operator

    def get_depth(self):
        return self.__depth

    def get_cost(self):
        return self.__cost

    def get_path_from_start(self):
        state_list = []
        moves = []

        current = self
        while current.get_operator() is not None:
            state_list.append(current.get_state())
            moves.append(current.get_operator())

        state_list.reverse()
        moves.reverse()

        for state in state_list:
            display(state)

        return moves


def create_node(state: int, parent, operator, depth, cost) -> Node:
    return Node(state, parent, operator, depth, cost)

def main() -> None:
    def create_list(choice: int) -> list:
        def generate_random_state() -> list:
            state = [i for i in range(10)]
            random.shuffle(state)
            return state

        if choice == 1:
            return generate_random_state()

        def take_input_generate_state() -> list:
            state = input("Enter state each followed by a , seperator: ")
            state = state.split(", ")
            return [int(i) for i in state]

        return take_input_generate_state()

    choice = int(input("1: Random generate state\n2: Manually entering state\n"))
    state = create_list(choice)

    start_time = time.clock()

    # get result

    end_time = time.clock()


if __name__ == "__main__":
    main()
