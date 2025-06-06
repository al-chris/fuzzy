import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy input variables
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')

# Define fuzzy output variable
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Auto-membership functions for inputs (poor, average, good)
food.automf(3)
service.automf(3)

# Custom membership functions for output (tip)
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Define fuzzy rules
rule1 = ctrl.Rule(food['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(food['good'] | service['good'], tip['high'])

# Create control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_sim = ctrl.ControlSystemSimulation(tipping_ctrl)

# Input values
tipping_sim.input['food'] = 6.5
tipping_sim.input['service'] = 9.8

# Compute the result
tipping_sim.compute()

# Output result
print(f"Recommended Tip: {tipping_sim.output['tip']:.2f}%")

# Visualize the result
tip.view(sim=tipping_sim)
plt.show()
