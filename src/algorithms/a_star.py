from Node import *
from commands.compare_commands import *


def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = [create_node(move_up(node.state), node, "up", node.depth + 1, 0),
                      create_node(move_down(node.state), node, "down", node.depth + 1, 0),
                      create_node(move_left(node.state), node, "left", node.depth + 1, 0),
                      create_node(move_right(node.state), node, "right", node.depth + 1, 0)]
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes


def perform_a_star(start, goal) -> list:
    # A star heuristic search
    nodes = [create_node(start, None, None, 0, 0)]
    explored = []
    count = 0

    compare = Compare()
    a_star_compare = AStarIDAStarCompareCommand
    invoker = Invoker()
    invoker.register(a_star_compare, "a_star_compare")

    while nodes:
        nodes.sort(invoker.execute("a_star_compare"))
        node = nodes.pop(0)
        explored.append(node.get_state())
        count += 1
        print("Trying state", node.get_state(), " and move: ", node.get_operator())
        if node.get_state() == goal:
            print("OK!")
            print(f"The number of nodes visited {count}")
            print("State of moves are as follows:")
            return node.get_path_from_start()

        expanded_nodes = expand_node(node)
        for item in expanded_nodes:
            state = item.get_state()
            if state not in explored:
                nodes.append(item)

    return nodes
