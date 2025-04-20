#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:55:25 2024

@author: rajeshgogineni
"""

from gurobipy import Model, GRB

# Create a new model
model = Model("week_1")

# Create variables
x = model.addVar(name="x", lb=0)  # x >= 0
y = model.addVar(name="y", lb=0)  # y >= 0

# Set objective: maximize
model.setObjective(3 * x + 4 * y, GRB.MAXIMIZE)

# Add constraint: 2 * x + y <= 8 and constraint: x + 2 * y <= 8
model.addConstr(2 * x + y <= 8, "c0")
model.addConstr(x + 2 * y <= 8, "c1")


# Optimize the model
model.optimize()

# Print the results
if model.status == GRB.OPTIMAL:
    print(f'Optimal solution found: x = {x.X}, y = {y.X}')
else:
    print('No optimal solution found')