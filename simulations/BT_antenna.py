import numpy as np
import matplotlib.pyplot as plt

Z = np.array([
    105.7554 - 24.5814j,
    97.2163 - 15.5316j,
    89.9550 - 6.5180j,
    83.7785 + 2.3938j,
    78.5234 + 11.1696j,
    75.4636 + 16.9378j,
    74.0534 + 19.7970j,
    70.2548 + 28.2778j,
    67.0339 + 36.6236j,
    64.3134 + 44.8518j,
    62.0299 + 52.9839j,
    60.1313 + 61.0434j
])

F = np.array([
    2300000000.000000,
    2330000000.000000,
    2360000000.000000,
    2390000000.000000,
    2420000000.000000,
    2440000000.000000,  # Frequency of interest for 2.44 GHz
    2450000000.000000,
    2480000000.000000,
    2510000000.000000,
    2540000000.000000,
    2570000000.000000,
    2600000000.000000
])

# Calculate the reflection coefficient Gamma
Gamma = (Z - 50) / (Z + 50)

# Identify the index of the point corresponding to 2.44 GHz
target_frequency = 2.44e9
target_index = np.where(F == target_frequency)[0][0]

# Plot all points on the Smith chart
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
ax.set_title("Smith Chart of Antenna Impedance", va='bottom')

# Plot each point; mark the point for 2.44 GHz in red
for i, gamma in enumerate(Gamma):
    color = 'red' if i == target_index else 'blue'
    ax.plot(np.angle(gamma), np.abs(gamma), 'o', color=color, markersize=6)

# Set radial limits and display the grid
ax.set_rlim(0, 1)
ax.grid(True)

# Show plot
plt.show()