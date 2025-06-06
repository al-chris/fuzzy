# Fuzzy Logic Examples in Python

This project contains two simple Python implementations of fuzzy logic systems using the `scikit-fuzzy` library:

1. **Fan Speed Controller** – Adjusts fan speed based on room temperature.
2. **Restaurant Tip Calculator** – Suggests tip amount based on food quality and service level.

These examples demonstrate how fuzzy logic can be used for approximate reasoning and decision-making, mimicking human intuition.

---

## Features

* Uses `scikit-fuzzy` to create fuzzy variables and rule-based systems.
* Defines custom membership functions for each input/output variable.
* Includes visualization of fuzzy sets and outputs.
* Shows how to fuzzify inputs and defuzzify the output.

---

## Requirements

* Python 3.6 or higher
* `scikit-fuzzy`
* `numpy`
* `matplotlib`

### Installation

Install dependencies with:

```bash
pip install scikit-fuzzy matplotlib numpy
```

---

## Example 1: Fan Speed Controller

### Description

Controls fan speed based on room temperature using fuzzy logic.

### Input

* Temperature (°C)

### Output

* Fan Speed (%)

### Fuzzy Rules

* IF temperature is **cold**, THEN fan speed is **low**
* IF temperature is **warm**, THEN fan speed is **medium**
* IF temperature is **hot**, THEN fan speed is **high**

### Run

```bash
python fan_controller.py
```

---

## Example 2: Restaurant Tip Calculator

### Description

Estimates the tip percentage based on the quality of food and service at a restaurant.

### Inputs

* Food quality (0–10)
* Service quality (0–10)

### Output

* Tip amount (%)

### Fuzzy Rules

* IF food is **poor** OR service is **poor**, THEN tip is **low**
* IF service is **average**, THEN tip is **medium**
* IF food is **good** OR service is **good**, THEN tip is **high**

### Run

```bash
python tip_calculator.py
```

---

## File Structure

```
.
├── fan_controller.py      # Fan speed controller using fuzzy logic
├── tip_calculator.py      # Restaurant tip calculator using fuzzy logic
├── README.md              # Project documentation
```

---

## Customization

These systems can be extended to handle additional inputs, outputs, or more complex rules. Example applications:

* Smart thermostats
* Vehicle speed control
* Risk assessment
* Health monitoring systems

---

## References

* [Scikit-Fuzzy GitHub](https://github.com/scikit-fuzzy/scikit-fuzzy)
* [Fuzzy Logic - Wikipedia](https://en.wikipedia.org/wiki/Fuzzy_logic)

---

## License

This project is licensed under the MIT License.