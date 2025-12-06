import time
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from QuickBench import monitor

# Test 1: As a decorator
@monitor
def heavy_task():
    time.sleep(0.1)
    return "Done"

# Test 2: As a context manager
def test_block():
    with monitor(label="Custom Block"):
        time.sleep(0.2)

if __name__ == "__main__":
    print("Testing Decorator:")
    heavy_task()
    
    print("\nTesting Context Manager:")
    test_block()