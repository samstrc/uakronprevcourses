import numpy as np # Import the libraries/modules we need
import random # Library used for random number generations

# Define the transition matrix and each of the states
transName = ['Healthy', 'Sick', 'Very Sick', 'Dead']
transMatrix = [
    [1.0, 0.0, 0.0, 0.0],  # Healthy
    [0.5, 0.2, 0.2, 0.1],  # Sick
    [0.0, 0.3, 0.4, 0.3],  # Very Sick
    [0.0, 0.0, 0.0, 1.0]   # Dead (RIP)
]

# Part d: Simulate the Markov chain for any starting state :))
def simulate_markov_chain(start_state, steps):
    current_state = start_state
    path = [current_state]
    probability = 1.0

    for step in range(steps):
        state_index = transName.index(current_state)
        next_state = random.choices(transName, weights=transMatrix[state_index])[0]
        probability *= transMatrix[state_index][transName.index(next_state)]
        path.append(next_state)
        current_state = next_state

    return path, probability

# Part e: Simulate 3 steps, starting from "Sick" five times
print("Part e: Simulations for 3 days starting from 'Sick'")
for i in range(5):
    path, prob = simulate_markov_chain('Sick', 3)
    print(f"Simulation {i + 1}: Path = {path}, Probability = {prob:.6f}")

# Part f: Simulate 10 days until paths end in both "Healthy" and "Dead"
print("\nPart f: Simulations for 10 days until one ends in 'Healthy' and another in 'Dead'")
healthy_found = False
dead_found = False
simulations_count = 0

while not (healthy_found and dead_found):
    simulations_count += 1
    path, prob = simulate_markov_chain('Sick', 10)
    if path[-1] == 'Healthy' and not healthy_found:
        healthy_found = True
        print(f"Path ending in 'Healthy': {path}, Probability = {prob:.6f}")
    if path[-1] == 'Dead' and not dead_found:
        dead_found = True
        print(f"Path ending in 'Dead': {path}, Probability = {prob:.6f}")

print(f"Total simulations to find both outcomes: {simulations_count}")