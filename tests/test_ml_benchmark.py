import sys
import os
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# --- PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# ------------------

from QuickBench import MLBencher
# Removed LLMBencher import

def test_ml_bench():
    print("\n--- Testing ML Bencher ---")
    X, y = make_classification(n_samples=50, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Run ML Benchmark
    bencher = MLBencher({"LogisticReg": model}, X_test, y_test)
    df = bencher.run()
    
    print(df)
    assert not df.empty
    assert "Primary Score" in df.columns or "F1 Score" in df.columns

if __name__ == "__main__":
    test_ml_bench()