import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Define fuzzy variables (input and output)
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')  # 0 to 40 °C
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')     # 0 to 100 %

# 2. Define membership functions
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 40])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [60, 100, 100])

# 3. Define fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])

# 4. Create control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# 5. Provide input and compute output
fan_sim.input['temperature'] = 28
fan_sim.compute()

# 6. Output the result
print(f"Fan Speed = {fan_sim.output['fan_speed']:.2f}%")

# 7. (Optional) Visualize the output
fan_speed.view(sim=fan_sim)
plt.show()
