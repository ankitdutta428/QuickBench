## QuickBench 

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

Usage
1. As a Decorator
Use @monitor to time a specific function.
```
from QuickBench import monitor
import time

@monitor
def heavy_computation():
    # Simulating work
    time.sleep(1.5)
    return "Done"

heavy_computation()

# Output: [heavy_computation] finished in 1.50 s
```

2. As a Context Manager
Use with monitor(): to time a specific chunk of logic.

```
from QuickBench import monitor
import time

def process_data():
    print("Preparing data...")
    
    with monitor(label="Database Query"):
        # Only time this specific part
        time.sleep(0.25)
    
    print("Finished.")

process_data()

# Output: [Database Query] finished in 250.00 ms
```
##

## Author: Ankit Dutta


