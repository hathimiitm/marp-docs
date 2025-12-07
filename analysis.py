# analysis.py — Marimo Notebook
# Email: 24f2005641@ds.study.iitm.ac.in
# This notebook demonstrates interactive variable dependencies in Marimo.

import marimo as mo

# --- CELL 1: Base data and widget -------------------------------------------
# This cell defines the base variables and an interactive slider.
# Other cells depend on `slider` and `base_value`.

slider = mo.ui.slider(1, 100, value=10)
base_value = 5

slider, mo.md(f"Selected value: **{slider.value}**")

# --- CELL 2: Computation depending on CELL 1 --------------------------------
# This cell computes a derived metric based on slider input.
# Data flow: slider.value -> multiplier -> result

multiplier = slider.value
result = base_value * multiplier

mo.md(f"""
### Computation Output  
Base value = {base_value}  
Multiplier (slider) = {multiplier}  
**Result = {result}**
""")

# --- CELL 3: Dynamic Markdown ------------------------------------------------
# This cell updates automatically when slider changes.
# Data flow: slider.value -> markdown visualization

bars = "🔵" * slider.value
mo.md(f"### Visual Indicator\n{bars}")
