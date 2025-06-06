import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Membership functions for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 40])

# Membership functions for fan speed
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [60, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])

# Control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# GUI setup
root = tk.Tk()
root.title("Fuzzy Fan Speed Controller")

# Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 2.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Function to compute and update plot
def update_fan_speed(val=None):
    temp_val = temp_slider.get()
    fan_sim.input['temperature'] = temp_val
    fan_sim.compute()
    result = fan_sim.output['fan_speed']
    result_var.set(f"{result:.2f} %")

    # Plot update
    ax.clear()
    ax.plot(fan_speed.universe, fan_speed['low'].mf, 'r', label='Low')
    ax.plot(fan_speed.universe, fan_speed['medium'].mf, 'g', label='Medium')
    ax.plot(fan_speed.universe, fan_speed['high'].mf, 'b', label='High')
    ax.axvline(result, color='k', linestyle='--', label=f'Speed = {result:.2f}%')
    ax.set_title('Fan Speed Membership & Output')
    ax.set_xlabel('Fan Speed (%)')
    ax.set_ylabel('Membership')
    ax.legend(loc='upper left')
    canvas.draw()

# Temperature slider
tk.Label(root, text="Room Temperature (°C)").pack()
temp_slider = tk.Scale(root, from_=0, to=40, orient=tk.HORIZONTAL, resolution=0.5, command=update_fan_speed)
temp_slider.set(25)
temp_slider.pack(fill='x', padx=10)

# Fan speed result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Initial computation
update_fan_speed()

# Run GUI
root.mainloop()
