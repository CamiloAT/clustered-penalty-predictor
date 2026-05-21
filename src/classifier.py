import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

class PenaltyClassifier:
    def __init__(self):
        # Multiclass classifier (0: Gol, 1: Atajada, 2: Fallo)
        self.model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42, class_weight='balanced')
            
    def fit(self, X: pd.DataFrame, y: pd.Series):
        """El DataFrame X ya debe tener la columna 'Cluster' inyectada"""
        self.model.fit(X, y)
        
    def predict(self, X: pd.DataFrame):
        return self.model.predict(X)
        
    def predict_proba(self, X: pd.DataFrame):
        return self.model.predict_proba(X)
        
    def save_model(self, filepath: str):
        joblib.dump(self.model, filepath)
        
    def load_model(self, filepath: str):
        self.model = joblib.load(filepath)
