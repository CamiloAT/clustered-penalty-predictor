import pandas as pd
from sklearn.cluster import KMeans
import joblib

class PenaltyClustering:
    def __init__(self, n_clusters: int = 4):
        self.n_clusters = n_clusters
        # Aplicamos K-Means estrictamente sobre las características solicitadas
        self.model = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)
        
    def fit(self, X: pd.DataFrame):
        self.model.fit(X)
        
    def predict(self, X: pd.DataFrame) -> pd.Series:
        return self.model.predict(X)
        
    def save_model(self, filepath: str):
        joblib.dump(self.model, filepath)
        
    def load_model(self, filepath: str):
        self.model = joblib.load(filepath)
