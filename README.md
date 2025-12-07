# QuickBench

<div align="center">
  <img src="assets/logo.png" alt="QuickBench Logo" width="300">
  <br>
</div>

### The Essential Performance Toolkit for Python.
#### A [Minerva AI] Project.

![Build Status](https://github.com/ankitdutta428/QuickBench/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)


A lightweight, zero-dependency Python utility for timing code execution. QuickBench provides both a **decorator** and a **context manager** which can easily measure how long functions or code blocks take to run.

**QuickBench** is the all-in-one performance toolkit for Python developers. Whether you are optimizing a `for` loop, comparing Machine Learning models, or evaluating LLM latency, QuickBench handles the metrics so you can focus on the code.

## Why QuickBench?

* **Universal Timer:** Benchmark functions or blocks of code with a simple decorator.
* **ML Benchmarking:** Automatically compare `sklearn`, `xgboost`, etc. (Accuracy, F1, RMSE).
* **LLM Benchmarking:** Measure Token/sec and Latency for GPT, Llama, or Claude wrappers.
* **pandas Output:** All results return clean DataFrames ready for analysis.

---

## Features

- **Decorator Support:** Time entire functions with a single line (`@monitor`).
- **Context Manager:** Time specific blocks of code inside a function (`with monitor():`).
- **Human Readable:** Automatically formats output to `ns`, `µs`, `ms`, or `s`.
- **Zero Dependencies:** Pure Python, no heavy libraries required.

## Installation


```bash
pip install QuickBench
```

## Tutorial

Tutorial & Usage
1. The Universal Timer (@monitor)
Stop writing start = time.time() manually. Use the decorator to time functions, or the context manager to time specific blocks.

A. Function Decorator Use this to measure how long a specific function takes to run.

```Python

from QuickBench import monitor
import time

@monitor
def heavy_processing():
    # Simulates a slow task
    time.sleep(1.5)
    return "Done"

heavy_processing()
# Output: [heavy_processing] finished in 1.50 s
```

B. Context Manager (Block Timer) Use this when you only want to time a few lines of code inside a larger function.

```Python

from QuickBench import monitor
import time

def data_pipeline():
    print("Loading data...")
    
    with monitor(label="Data Cleaning"):
        # Time only this specific part
        time.sleep(0.3)
    
    print("Pipeline finished.")
```
2. The Auto-ML Benchmarker
QuickBench automatically detects if your problem is Classification or Regression and calculates the correct metrics (Accuracy/F1 vs. MSE/R2).

Step 1: Define your models You can use any model that follows the scikit-learn API (has .predict()).

```Python

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

models = {
    "Logistic": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}
```
Step 2: Run the Benchmark Pass your dictionary of models along with your test data.

```Python

from QuickBench.ai import MLBencher

# Assuming you have X_test and y_test ready
bencher = MLBencher(models, X_test, y_test)
results = bencher.run()

print(results)
```
**Output (Returns a Pandas DataFrame):**

| Model Type | Name | Primary Score | F1 Score | Latency (s) |
| :--- | :--- | :--- | :--- | :--- |
| Classification | Random Forest | 0.9820 | 0.9815 | 0.1204 |
| Classification | Decision Tree | 0.9650 | 0.9648 | 0.0052 |
| Classification | Logistic | 0.9400 | 0.9390 | 0.0021 |


## Contributing & Issues
We would absolutely love your contribution, since that is what makes us keep going. Found a bug? Want to add a feature?

#### Report Issues: [GitHub Issues Page](https://github.com/ankitdutta428/QuickBench/issues)

#### Source Code: [GitHub Repository](https://github.com/ankitdutta428/QuickBench)

## Branding
QuickBench is proudly developed and maintained by Minerva AI under the able leadership of Ankit Dutta. Empowering developers with wisdom and speed.


