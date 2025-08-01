from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np
import math

def create_quantum_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        qc.ry(np.pi/2, i)
    qc.measure_all()
    return qc

def simulate(qc):
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000000)
    result = job.result()
    counts = result.get_counts()

    base_10_counts = {int(k, 2): v for k, v in counts.items()}

    plt.bar(base_10_counts.keys(), base_10_counts.values())
    plt.show()

def generate_random_number(upper_bound=None):
    MAX_UPPER_BOUND = 1000000
    MAX_QUBITS = 20
    
    if upper_bound is None:
        num_qubits = 8
        max_value = 2**num_qubits - 1
    else:
        if upper_bound <= 0:
            raise ValueError("Upper bound must be a positive integer")
        
        if upper_bound > MAX_UPPER_BOUND:
            raise ValueError(f"Upper bound cannot exceed {MAX_UPPER_BOUND}")
        
        num_qubits = max(1, math.ceil(math.log2(upper_bound + 1)))
        num_qubits = min(num_qubits, MAX_QUBITS)
        max_value = upper_bound
    
    qc = create_quantum_circuit(num_qubits)
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    raw_value = int(list(counts.keys())[0], 2)
    
    return raw_value % (max_value + 1)

def main():
    try:
        user_input = input("Enter upper bound for random number (press Enter for default, max 1,000,000): ")
        if user_input.strip():
            upper_bound = int(user_input)
            print(f"Generating random number between 0 and {upper_bound}...")
            random_num = generate_random_number(upper_bound)
        else:
            random_num = generate_random_number()
        
        print(f"Random number: {random_num}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()