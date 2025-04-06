import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')  # Sets up polar projection
a = 2
rad = np.arange(0, (2 * np.pi), 0.001)  # Creates an array of values from 0 to 2pi with a step size of 0.001
r_values = []

for t in rad:
    r = a*a  * np.cos(2 * t)
    if r >= 0:  # Check if the value is non-negative
        r_values.append(np.sqrt(r))
    else:
        r_values.append(np.nan)  # Append NaN (not a number) to avoid plotting invalid values

plt.polar(rad, r_values, 'g.')  # Plots the graph for each angle
plt.title("Lemniscate of Bernoulli")
plt.show()
