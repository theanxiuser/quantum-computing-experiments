# Quantum Algorithms

Implementations and experiments with quantum algorithms
using NumPy/Qiskit.

## Algorithms

| No. | Algorithm | Implementation |
|---|---|---|
| 01 | Deutsch | Completed |
| 02 | Deutsch-Jozsa | Planned | 
| 03 | Bernstein-Vazirani | Planned |
| 04 | Simon | Completed | 
| 04 | Quantum Fourier Transform (QFT) | Completed | 
| 04 | Quantum Phase Estimation (QPE) | Completed | 
| 05 | Grover | Planned | 
| 06 | Shor | Planned | 

## Structure

- `common/`: Reusable quantum utilities, currently only used by Deutsch algorithm.
- Each algorithm directory contains its mathematical
  implementation, Qiskit implementation, and documentation.

## Technologies

- Python
- NumPy
- Qiskit
- Qiskit Aer
- Matplotlib