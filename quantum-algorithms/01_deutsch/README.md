# Deutsch's Algorithm

## Overview

Deutsch's algorithm is an early example of a quantum
algorithm that demonstrates a computational advantage
over deterministic classical query complexity.

It determines whether a Boolean function

f: {0,1} -> {0,1}

is constant or balanced using one oracle query.

## Mathematical Background

The oracle is defined as:

U_f |x,y> = |x, y XOR f(x)>

The algorithm uses two qubits:

1. Input qubit
2. Auxiliary qubit

## Circuit Steps

1. Initialize |01>
2. Apply H tensor H
3. Apply the oracle U_f
4. Apply H tensor I
5. Measure the input qubit

## Implementations

- deutsch_numpy.ipynb
- deutsch_qiskit.ipynb

## Expected Results

| Function | Classification |
|---|---|
| f(x) = 0 | Constant |
| f(x) = 1 | Constant |
| f(x) = x | Balanced |
| f(x) = NOT x | Balanced |

## Learning Objectives

- Quantum superposition
- Tensor products
- Quantum oracle construction
- Phase kickback
- Quantum interference
- Measurement probabilities