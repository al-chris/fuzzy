# Fuzzy Logic & Image Processing Examples in Python

This project contains several Python implementations of fuzzy logic systems and a simple image processing example. It demonstrates fuzzy decision-making and basic computer vision, with both command-line and GUI interfaces.

## Main Features

- **Fan Speed Controller** – Adjusts fan speed based on room temperature using fuzzy logic.
- **Restaurant Tip Calculator** – Suggests tip amount based on food and service quality.
- **AI Decision Making (Loan Approval)** – Uses fuzzy logic to estimate loan approval likelihood based on income and credit score.
- **Image Processing** – Demonstrates edge detection on images using OpenCV.
- **Graphical User Interfaces (GUI)** – Interactive GUIs for all fuzzy logic examples (see `gui/` folder).

---

## Requirements

- Python 3.6 or higher
- `scikit-fuzzy`
- `numpy`
- `matplotlib`
- `opencv-python` (for image processing)
- `tkinter` (for GUIs, included with most Python installations)

### Installation

Install dependencies with:

```bash
pip install scikit-fuzzy matplotlib numpy opencv-python
```

---

## Examples

### 1. Fan Speed Controller
Controls fan speed based on room temperature using fuzzy logic.
- **Run (CLI):**
  ```bash
  python fan_controller.py
  ```
- **Run (GUI):**
  ```bash
  python gui/fan_controller_gui.py
  ```

### 2. Restaurant Tip Calculator
Estimates tip percentage based on food and service quality.
- **Run (CLI):**
  ```bash
  python tip_calculator.py
  ```
- **Run (GUI):**
  ```bash
  python gui/tip_calculator_gui.py
  ```

### 3. AI Decision Making (Loan Approval)
Estimates loan approval likelihood based on income and credit score.
- **Run (CLI):**
  ```bash
  python ai_decision_making.py
  ```
- **Run (GUI):**
  ```bash
  python gui/ai_decision_making_gui.py
  ```

### 4. Image Processing Example
Performs edge detection on a sample image using OpenCV.
- **Run:**
  ```bash
  python image_processing.py
  ```
  (Make sure the image path in the script matches an image in the `images/` folder.)

---

## File Structure

```
.
├── ai_decision_making.py         # Fuzzy loan approval (CLI)
├── fan_controller.py             # Fan speed controller (CLI)
├── tip_calculator.py             # Restaurant tip calculator (CLI)
├── image_processing.py           # Image edge detection example
├── gui/
│   ├── ai_decision_making_gui.py # Loan approval GUI
│   ├── fan_controller_gui.py     # Fan controller GUI
│   └── tip_calculator_gui.py     # Tip calculator GUI
├── images/                       # Sample images for processing
├── README.md                     # Project documentation
├── pyproject.toml                # Project dependencies
```

---

## Customization & Extensions

These systems can be extended to handle additional inputs, outputs, or more complex rules. Example applications:

- Smart thermostats
- Vehicle speed control
- Risk assessment
- Health monitoring systems
- Computer vision tasks

---

## References

- [Scikit-Fuzzy GitHub](https://github.com/scikit-fuzzy/scikit-fuzzy)
- [Fuzzy Logic - Wikipedia](https://en.wikipedia.org/wiki/Fuzzy_logic)
- [OpenCV Documentation](https://docs.opencv.org/)

---

## License

This project is licensed under the [MIT License](LICENSE).
