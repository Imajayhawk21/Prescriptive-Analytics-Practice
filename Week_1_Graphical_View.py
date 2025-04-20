#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:53:25 2024

@author: rajeshgogineni
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the constraints as functions
def constraint1(x):
    return (8 - 2*x)  # y <= 8 - 2x

def constraint2(x):
    return (8 - x)/2  # y <= (8 - x)/2

# Create x values (0 to the maximum possible value based on constraints)
x = np.linspace(0, 8, 400)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the constraint lines
plt.plot(x, constraint1(x), label=r'$2x + y \leq 8$', color='blue')
plt.plot(x, constraint2(x), label=r'$x + 2y \leq 8$', color='green')

# Set the axes limits
plt.xlim((0, 8))
plt.ylim((0, 8))

# Fill the feasible region (where both constraints and non-negativity hold)
plt.fill_between(x, np.minimum(constraint1(x), constraint2(x)), 0, color='gray', alpha=0.3)

# Add labels and title
plt.title('Feasible Region for Linear Programming Problem')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()