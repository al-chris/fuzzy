import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import messagebox

# Step 1: Define fuzzy variables
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Step 2: Define membership functions
food.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Step 3: Define fuzzy rules
rule1 = ctrl.Rule(service['poor'] | food['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | food['good'], tip['high'])

# Step 4: Create control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_sim = ctrl.ControlSystemSimulation(tipping_ctrl)

# Step 5: GUI setup
def calculate_tip():
    try:
        food_val = float(food_entry.get())
        service_val = float(service_entry.get())

        if not (0 <= food_val <= 10) or not (0 <= service_val <= 10):
            raise ValueError("Inputs must be between 0 and 10.")

        tipping_sim.input['food'] = food_val
        tipping_sim.input['service'] = service_val
        tipping_sim.compute()

        result = tipping_sim.output['tip']
        result_label.config(text=f"Recommended Tip: {result:.2f}%")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Create main window
root = tk.Tk()
root.title("Fuzzy Tip Calculator")

tk.Label(root, text="Food Quality (0–10):").grid(row=0, column=0, padx=10, pady=5)
food_entry = tk.Entry(root)
food_entry.grid(row=0, column=1)

tk.Label(root, text="Service Quality (0–10):").grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(root)
service_entry.grid(row=1, column=1)

calculate_btn = tk.Button(root, text="Calculate Tip", command=calculate_tip)
calculate_btn.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Recommended Tip: --%")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
