import numpy as np


def deutsch_oracle(f):
    """
    Construct Deutsch's oracle U_f.

    U_f |x,y> = |x, y XOR f(x)>

    Basis ordering:
        |00>, |01>, |10>, |11>
    """

    U = np.zeros((4, 4), dtype=complex)

    for x in (0, 1):
        for y in (0, 1):

            output_y = y ^ f(x)

            input_index = 2 * x + y
            output_index = 2 * x + output_y

            U[output_index, input_index] = 1

    return U


# Four Boolean functions

def constant_zero(x):
    return 0


def constant_one(x):
    return 1


def identity(x):
    return x


def negation(x):
    return 1 - x


DEUTSCH_FUNCTIONS = {
    "constant_zero": constant_zero,
    "constant_one": constant_one,
    "identity": identity,
    "negation": negation
}
