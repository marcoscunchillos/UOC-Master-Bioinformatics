# 🧩 Module 01: Computational Thinking for Programming

[![Status](https://img.shields.io/badge/Status-In_Progress-blue?style=flat-square)](#)
[![Language](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)](#)

## 🎯 Overview
This module establishes the core principles of **computational thinking**—problem decomposition, pattern recognition, abstraction, and algorithm design. Exercises are mapped directly to biological contexts, such as parsing genetic sequences, calculating environmental toxicity thresholds, and modeling cell growth curves.

---

## 🚀 Key Competencies

> 1. **Decomposition:** Breaking complex biomedical problems into modular functions.
> 2. **Pattern Recognition:** Identifying recurring structures in DNA/RNA strings and chemical concentration matrices.
> 3. **Abstraction:** Translating real-world toxicological parameters into clean Python variables and data types.
> 4. **Algorithmic Logic:** Designing control flows for patient cohort filtering and risk assessment.

---

## 📊 Practical Assignments (PECs)

| Assignment | Topic | Key Implementation |
| :--- | :--- | :--- |
| **PEC 1** | *Logic & Flow Control* | Conditionals and loops applied to toxicity threshold evaluation. |
| **PEC 2** | *Data Structures & Functions* | Lists, dictionaries, and functions for handling patient biomarker records. |
| **PEC 3** | *Final Algorithmic Project* | End-to-end Python script processing environmental exposure metrics. |

---

## 💻 Code Sample: Exposure Threshold Filter

```python
# Abstraction: Classifying exposure risk based on threshold values
def evaluate_exposure(concentration_ppm, threshold=0.05):
    if concentration_ppm >= threshold:
        return "HIGH_RISK: Exceeds safe limit"
    return "SAFE: Below threshold"

print(evaluate_exposure(0.082))  # HIGH_RISK: Exceeds safe limit