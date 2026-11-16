import numpy as np

# Computational basis states

ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)

# Superposition states

PLUS = (ZERO + ONE) / np.sqrt(2)
MINUS = (ZERO - ONE) / np.sqrt(2)


def basis_state(*bits):
    """
    Construct a computational basis state.

    Example:
        basis_state(0, 1) -> |01>
    """
    state = np.array([1], dtype=complex)

    for bit in bits:
        if bit not in (0, 1):
            raise ValueError("Bits must be 0 or 1")

        state = np.kron(state, ZERO if bit == 0 else ONE)

    return state


def normalize(state):
    """Normalize a quantum state."""
    norm = np.linalg.norm(state)

    if np.isclose(norm, 0):
        raise ValueError("Cannot normalize zero state")

    return state / norm


def probabilities(state):
    """Calculate measurement probabilities."""
    return np.abs(state) ** 2
