import pickle
import json
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor

def train_model(repo_path):
    X_train_scaled = pd.read_csv(f'{repo_path}/data/processed_data/X_train_scaled.csv')
    y_train = pd.read_csv(f'{repo_path}/data/processed_data/y_train.csv')

    with open(f'{repo_path}/models/parameters.json', 'rb') as file:
        params = json.load(file)

    model = RandomForestRegressor(**params)
    model.fit(X_train_scaled, y_train)
    with open(f'{repo_path}/models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    repo_path = os.getcwd()
    train_model(repo_path)