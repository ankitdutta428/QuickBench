import time
import pandas as pd
# Import both Classification and Regression metrics
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score,
    mean_squared_error, r2_score
)
import numpy as np

class MLBencher:
    def __init__(self, models: dict, X_test, y_test):
        self.models = models
        self.X_test = X_test
        self.y_test = y_test
        self.results = []
        
        # Determine problem type based on target variable's nature
        # If the target has few unique, discrete values (like 0, 1, 2), assume Classification
        # Otherwise, assume Regression
        if len(np.unique(y_test)) <= 20 and all(i == int(i) for i in y_test):
            self.problem_type = "Classification"
        else:
            self.problem_type = "Regression"

    def run(self):
        print(f"📊 Starting ML Benchmark ({self.problem_type}) on {len(self.models)} models...")
        
        for name, model in self.models.items():
            # 1. Measure Inference Time
            start = time.perf_counter()
            y_pred = model.predict(self.X_test)
            elapsed = time.perf_counter() - start
            
            # 2. Calculate Metrics based on Problem Type
            
            if self.problem_type == "Classification":
                acc = accuracy_score(self.y_test, y_pred)
                f1 = f1_score(self.y_test, y_pred, average='weighted', zero_division=0)
                prec = precision_score(self.y_test, y_pred, average='weighted', zero_division=0)
                
                self.results.append({
                    "Model Type": "Classification",
                    "Name": name,
                    "Primary Score": round(acc, 4),
                    "F1 Score": round(f1, 4),
                    "Precision": round(prec, 4),
                    "Metric 4": "N/A",
                    "Latency (s)": round(elapsed, 4)
                })
            
            elif self.problem_type == "Regression":
                # Metrics for continuous output
                r2 = r2_score(self.y_test, y_pred)
                mse = mean_squared_error(self.y_test, y_pred)
                rmse = np.sqrt(mse) # Root Mean Squared Error (more interpretable)
                
                self.results.append({
                    "Model Type": "Regression",
                    "Name": name,
                    "Primary Score": round(r2, 4),
                    "R-Squared": round(r2, 4),
                    "MSE": round(mse, 4),
                    "RMSE": round(rmse, 4),
                    "Latency (s)": round(elapsed, 4)
                })
            
        # For Classification, we sort by F1 Score (higher is better)
        if self.problem_type == "Classification":
            sort_key = "F1 Score"
            ascending = False
        # For Regression, we sort by R-Squared (higher is better)
        else:
            sort_key = "R-Squared"
            ascending = False

        return pd.DataFrame(self.results).sort_values(by=sort_key, ascending=ascending)