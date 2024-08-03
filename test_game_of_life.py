import pytest


def evolve(initial_state):
    # fill this out
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]
    moves += [(0, 1), (1, -1), (1, 0), (1, 1)]
    new_state = []
    for i in range(len(initial_state)):
        new_state.append([-1] * len(initial_state[0]))
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            ones, zeros = 0, 0
            for move in moves:
                x, y = i + move[0], j + move[1]
                if (
                    x >= len(initial_state)
                    or y >= len(initial_state[0])
                    or x < 0
                    or y < 0
                ):
                    continue
                if initial_state[x][y] == 0:
                    zeros += 1
                else:
                    ones += 1
            if initial_state[i][j] == 1 and (ones < 2 or ones > 3):
                new_state[i][j] = 0
            elif initial_state[i][j] == 0 and ones == 3:
                new_state[i][j] = 1
            else:
                new_state[i][j] = initial_state[i][j]
    return new_state


test_case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

test_case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


# adding pytest based unit tests
@pytest.mark.parametrize(
    "initial_state, evolved_state",
    [(test_case_1, test_case_1), (test_case_2, test_case_2_next)],
)
def test_evolve(initial_state, evolved_state):
    assert evolve(initial_state) == evolved_state
