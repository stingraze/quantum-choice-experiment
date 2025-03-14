# (C)Tsubasa Kato - 2025/3/14 9:18AM
# Made with the help of Jan.ai using Phi-4 from Microsoft.
import random

def hadamard(qubit):
    if qubit == 0:
        return random.choice([0, 1])
    elif qubit == 1:
        return random.choice([0, 1])

def cnot(control, target):
    if control == 1:
        target = 1 - target
    return target

def create_entangled_pair():
    qubit_a = 0
    qubit_b = 0
    
    qubit_a = hadamard(qubit_a)
    qubit_b = cnot(qubit_a, qubit_b)

    return (qubit_a, qubit_b)

def measure_entangled_pair():
    qubit_a, qubit_b = create_entangled_pair()

    if random.random() < 0.5:
        qubit_a_measured = 0
    else:
        qubit_a_measured = 1
    
    if qubit_a == qubit_a_measured:
        qubit_b_measured = cnot(qubit_a, qubit_b)
    else:
        qubit_b_measured = 1 - cnot(qubit_a, qubit_b)

    return qubit_a_measured, qubit_b_measured

def make_choice_based_on_entanglement(activities):
    if len(activities) < 2:
        print("Please provide at least two activities to choose from.")
        return
    
    # Measure entangled pair
    qubit_a, _ = measure_entangled_pair()
    
    # Decision based on measurement results
    choice_index = qubit_a  # Use the result of qubit_a (0 or 1) for indexing

    print(f"Based on entangled qubits, you should {activities[choice_index]} today!")

def main():
    print("Enter two activities to choose from:")
    activity1 = input("Activity 1: ").strip()
    activity2 = input("Activity 2: ").strip()

    activities = [activity1, activity2]

    make_choice_based_on_entanglement(activities)

if __name__ == "__main__":
    main()
