import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
income = ctrl.Antecedent(np.arange(0, 101, 1), 'income')       # in $1000s
credit = ctrl.Antecedent(np.arange(0, 101, 1), 'credit')       # credit score 0-100
approval = ctrl.Consequent(np.arange(0, 101, 1), 'approval')   # approval likelihood %

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

# Input example
approval_sim.input['income'] = 40
approval_sim.input['credit'] = 60
approval_sim.compute()

print(f"Loan Approval Likelihood: {approval_sim.output['approval']:.2f}%")
