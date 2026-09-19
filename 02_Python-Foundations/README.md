# 🐍 30 Days of Python: Foundations for Health Data Science

<div align="left">

[![Status](https://img.shields.io/badge/Status-In_Progress-blue?style=flat-square)](#)
[![Language](https://img.shields.io/badge/Language-Python_3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![Focus](https://img.shields.io/badge/Focus-Exposomics_%26_Cancer_Research-green?style=flat-square)](#)

</div>

## 🎯 Overview
This directory tracks my daily progression through the **30 Days of Python** challenge. Rather than using standard generic programming examples, every script and exercise is contextualized around **Exposomics, Toxicological Modeling, Biomarkers, and Cancer Epidemiology** to build practical coding fluency for PhD research applications.

---

## 🎯 Core Principles
- **Manual Coding Mastery:** Built entirely without AI suggestions/autocompletions to ensure deep memory retention of Python syntax and algorithmic logic.
- **Biomedical Contextualization:** Translating basic concepts (operators, data structures, control flow) into biological metrics (dose-response curves, cell viability, exposure thresholds).
- **Clean Version Control:** Maintaining modular, executable, and well-commented Python scripts.

---

## 📊 Progress Tracker

| Day | Topic | Focus & Bio-Context | Script File |
| :---: | :--- | :--- | :---: |
| **01** | *Introduction & Basics* | Environment setup, basic operators, and Euclidean distance in exposure mapping. | [`01_operators.py`](./01_operators.py) |
| **02** | *Variables & Built-in Functions* | Variable declaration, type casting, and CLI patient/exposure input handling. | [`02_variables.py`](./02_variables.py) |
| **03** | *Operators & Boolean Logic* | Linear/quadratic dose-response curves, toxicity thresholds, and logical operators. | [`03_operators.py`](./03_operators.py) |
| **04** | *Strings & Text Parsing* | *Upcoming: Parsing biological sequences, chemical formulas, and biomarker names.* | `--` |
| **05** | *Lists & Data Collections* | *Upcoming: Managing patient cohorts and chemical concentration lists.* | `--` |

---

## 🧪 Code Sample: Toxicity Threshold Logic (Day 3)

```python
# Quadratic toxicity threshold evaluation (y = x^2 + 6x + 9)
# Finding the concentration 'x' at which toxicity 'y' equals 0
x_val = -3
y_val = x_val**2 + 6 * x_val + 9

print(f"Toxicity level y is {y_val} when exposure concentration x is {x_val}")
# Output: Toxicity level y is 0 when exposure concentration x is -3