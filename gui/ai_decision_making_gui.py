import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define fuzzy variables
income = ctrl.Antecedent(np.arange(0, 101, 1), 'income')      # 0-100 (thousands)
credit = ctrl.Antecedent(np.arange(0, 101, 1), 'credit')      # 0-100 (credit score)
approval = ctrl.Consequent(np.arange(0, 101, 1), 'approval')  # 0-100 (% likelihood)

# Membership functions
income['low'] = fuzz.trimf(income.universe, [0, 0, 50])
income['medium'] = fuzz.trimf(income.universe, [30, 50, 70])
income['high'] = fuzz.trimf(income.universe, [50, 100, 100])

credit['poor'] = fuzz.trimf(credit.universe, [0, 0, 50])
credit['fair'] = fuzz.trimf(credit.universe, [30, 50, 70])
credit['good'] = fuzz.trimf(credit.universe, [50, 100, 100])

approval['low'] = fuzz.trimf(approval.universe, [0, 0, 50])
approval['medium'] = fuzz.trimf(approval.universe, [30, 50, 70])
approval['high'] = fuzz.trimf(approval.universe, [50, 100, 100])

# Rules
rule1 = ctrl.Rule(income['low'] | credit['poor'], approval['low'])
rule2 = ctrl.Rule(credit['fair'], approval['medium'])
rule3 = ctrl.Rule(income['high'] & credit['good'], approval['high'])

# Control system
approval_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
approval_sim = ctrl.ControlSystemSimulation(approval_ctrl)

# GUI setup
root = tk.Tk()
root.title("Fuzzy Loan Approval")

# Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Update function
def update_approval(val=None):
    inc_val = income_slider.get()
    cred_val = credit_slider.get()
    approval_sim.input['income'] = inc_val
    approval_sim.input['credit'] = cred_val
    approval_sim.compute()
    result = approval_sim.output['approval']
    result_var.set(f"{result:.2f} %")

    ax.clear()
    ax.plot(approval.universe, approval['low'].mf, 'r', label='Low')
    ax.plot(approval.universe, approval['medium'].mf, 'g', label='Medium')
    ax.plot(approval.universe, approval['high'].mf, 'b', label='High')
    ax.axvline(result, color='k', linestyle='--', label=f'Approval = {result:.2f}%')
    ax.set_title('Loan Approval Membership & Output')
    ax.set_xlabel('Approval Likelihood (%)')
    ax.set_ylabel('Membership')
    ax.legend(loc='upper left')
    canvas.draw()

# Income slider
tk.Label(root, text="Income (thousands $)").pack()
income_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, resolution=1, command=update_approval)
income_slider.set(50)
income_slider.pack(fill='x', padx=10)

# Credit score slider
tk.Label(root, text="Credit Score (0-100)").pack()
credit_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, resolution=1, command=update_approval)
credit_slider.set(50)
credit_slider.pack(fill='x', padx=10)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Initial update
update_approval()

root.mainloop()
