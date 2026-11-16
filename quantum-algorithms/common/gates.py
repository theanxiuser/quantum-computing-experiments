import numpy as np

# Single-qubit gates

I = np.eye(2, dtype=complex)

X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

Y = np.array([
    [0, -1j],
    [1j, 0]
], dtype=complex)

Z = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
], dtype=complex)


def CNOT():
    """Two-qubit controlled-NOT gate."""
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ], dtype=complex)


def tensor(*operators):
    """Calculate the tensor product of multiple operators."""
    result = operators[0]

    for operator in operators[1:]:
        result = np.kron(result, operator)

    return result
