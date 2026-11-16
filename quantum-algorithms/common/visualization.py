import numpy as np


def print_state(state, threshold=1e-10):
    """Display a quantum state using computational basis notation."""

    n_qubits = int(np.log2(len(state)))

    if 2 ** n_qubits != len(state):
        raise ValueError("State dimension must be a power of 2")

    terms = []

    for index, amplitude in enumerate(state):

        if abs(amplitude) > threshold:

            basis = format(index, f"0{n_qubits}b")

            terms.append(
                f"({amplitude.real:.3f}"
                f"{amplitude.imag:+.3f}j)|{basis}>"
            )

    print(" + ".join(terms))


def print_probabilities(state):
    """Display measurement probabilities."""

    n_qubits = int(np.log2(len(state)))

    for index, amplitude in enumerate(state):

        probability = abs(amplitude) ** 2

        if probability > 1e-10:

            basis = format(index, f"0{n_qubits}b")

            print(f"|{basis}> : {probability:.4f}")
