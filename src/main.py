import random
import time
from algorithms.handler import Solve


def display(state: list) -> None:
    print("-------------")
    print(f"| {state[0]} | {state[1]} | {state[2]} |")
    print("-------------")
    print(f"| {state[3]} | {state[4]} | {state[5]} |")
    print("-------------")
    print(f"| {state[0]} | {state[7]} | {state[8]} |")
    print("-------------")

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

    solve = Solve(state, [1, 2, 3, 8, 0, 4, 7, 6, 5])
    result = solve.a_star()

    end_time = time.clock()
    if result is None:
        print("No solution")
    elif result == [None]:
        print("start node is the goal")

    else:
        print(result)
        print(f"{len(result)} moves")

    total_time = end_time - start_time
    print(f"Total time: {total_time}")

if __name__ == "__main__":
    main()
