import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define fuzzy variables
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Membership functions
food.automf(3)
service.automf(3)
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Rules
rule1 = ctrl.Rule(service['poor'] | food['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | food['good'], tip['high'])

# Control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_sim = ctrl.ControlSystemSimulation(tipping_ctrl)

# GUI setup
root = tk.Tk()
root.title("Fuzzy Tip Calculator")

# Plot setup
fig, ax = plt.subplots(figsize=(5, 2.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Function to compute tip and plot
def update_tip(val=None):
    food_val = food_slider.get()
    service_val = service_slider.get()
    tipping_sim.input['food'] = food_val
    tipping_sim.input['service'] = service_val
    tipping_sim.compute()
    result = tipping_sim.output['tip']
    result_var.set(f"{result:.2f} %")

    # Clear and replot without spawning new figures
    ax.clear()
    ax.plot(tip.universe, tip['low'].mf, 'r', label='Low')
    ax.plot(tip.universe, tip['medium'].mf, 'g', label='Medium')
    ax.plot(tip.universe, tip['high'].mf, 'b', label='High')
    ax.axvline(result, color='k', linestyle='--', label=f'Tip = {result:.2f}%')
    ax.set_title('Tip Membership & Output')
    ax.set_xlabel('Tip (%)')
    ax.set_ylabel('Membership')
    ax.legend(loc='upper left')
    canvas.draw()

# Sliders
tk.Label(root, text="Food Quality (0–10)").pack()
food_slider = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.1, command=update_tip)
food_slider.set(5)
food_slider.pack(fill='x', padx=10)

tk.Label(root, text="Service Quality (0–10)").pack()
service_slider = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.1, command=update_tip)
service_slider.set(5)
service_slider.pack(fill='x', padx=10)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Initial update
update_tip()

# Run GUI
root.mainloop()
