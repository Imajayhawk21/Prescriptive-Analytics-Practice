#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:43:29 2024

@author: rajeshgogineni
"""

from gurobipy import Model, GRB

# Create a new model
model = Model("test_model")

# Create variables
x = model.addVar(name="x", lb=0)  # x >= 0
y = model.addVar(name="y", lb=0)  # y >= 0

# Set objective: maximize x + 2y
model.setObjective(x + 2 * y, GRB.MAXIMIZE)

# Add constraint: x + y <= 10
model.addConstr(x + y <= 10, "c0")

# Optimize the model
model.optimize()

# Print the results
if model.status == GRB.OPTIMAL:
    print(f'Optimal solution found: x = {x.X}, y = {y.X}')
else:
    print('No optimal solution found')
