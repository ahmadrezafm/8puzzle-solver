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

        # for state in state_list:
        #     display(state)

        return moves

def create_node(state: int, parent, operator, depth, cost) -> Node:
    return Node(state, parent, operator, depth, cost)

def move_up(state):
    new_state = state[:]
    index = new_state.index(0)

    if index not in [0, 1, 2]:
        new_state[index], new_state[index-3] = new_state[index-3], new_state[index]
        return new_state

    return None

def move_down(state):
    new_state = state[:]
    index = new_state.index(0)

    if index not in [6, 7, 8]:
        new_state[index], new_state[index+3] = new_state[index+3], new_state[index]
        return new_state

    return None

def move_left(state):
    new_state = state[:]
    index = new_state.index(0)

    if index not in [0, 3, 6]:
        new_state[index], new_state[index-1] = new_state[index-1], new_state[index]
        return new_state

    return None

def move_right(state):
    new_state = state[:]
    index = new_state.index(0)

    if index not in [2, 5, 8]:
        new_state[index], new_state[index+1] = new_state[index+1], new_state[index]
        return new_state

    return None

