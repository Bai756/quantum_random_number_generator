# Quantum Random Number Generator

A web application that generates truly random numbers using quantum computing, built with Flask and Qiskit.

## Features

- Generate random numbers up to 1,000,000 (20 qubits)
- Simple web interface
- Powered by IBM's Qiskit quantum simulator

## How It Works

1. A quantum circuit is created with enough qubits to cover your upper bound.
2. Each qubit is placed in superposition.
3. The circuit is measured, producing a random binary number.
4. The result is converted to an integer within your specified range.
