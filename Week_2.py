#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:17:21 2024

@author: rajeshgogineni
"""

from gurobipy import Model, GRB

# Create a new model
model = Model("week_2")

# Create variables
x = model.addVar(name="x", lb=0)  # x >= 0
y = model.addVar(name="y", lb=0)  # y >= 0

# Set objective:
model.setObjective(4 * x + 3 * y, GRB.MAXIMIZE)

# Add constraint for 
model.addConstr(3 * x + 2 * y <= 12, "c0")
model.addConstr(2 * x + 3 * y <= 9, "c1")
model.addConstr(x + y <= 5, "c2")

# Optimize the model
model.optimize()

# Print the results
if model.status == GRB.OPTIMAL:
    print(f'Optimal solution found: x = {x.X}, y = {y.X}')
else:
    print('No optimal solution found')