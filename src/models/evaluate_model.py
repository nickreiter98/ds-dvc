import pickle
import os
import json
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(repo_path):
    X_test_scaled = pd.read_csv(f'{repo_path}/data/processed_data/X_test_scaled.csv')
    y_test = pd.read_csv(f'{repo_path}/data/processed_data/y_test.csv')

    with open(f'{repo_path}/models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics = {
        'MSE': str(mse),
        'MAE': str(mae),
        'r2': str(r2)
    }

    with open(f'{repo_path}/metrics/scores.json', 'w') as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    repo_path = os.getcwd()
    evaluate_model(repo_path)