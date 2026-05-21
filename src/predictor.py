import pandas as pd
import numpy as np

class PenaltyPredictor:
    def __init__(self, preprocessor, clustering_model, classifier_model):
        self.preprocessor = preprocessor
        self.clustering_model = clustering_model
        self.classifier_model = classifier_model
        
    def predict(self, raw_input: dict) -> dict:
        """
        Recibe situación hipotética, aplica aumentación, asigna clúster
        y retorna probabilidades matemáticas exactas.
        """
        df = pd.DataFrame([raw_input])
        
        # Rellenar columnas faltantes requeridas para que el Feature Engineering no falle
        defaults = {
            'Game_id': 0, 'OnTarget': 0, 'Goal': 0, 
            'Keeper': 'Desconocido', 'Elimination': 0, 'Penalty_Number': 1
        }
        for col, val in defaults.items():
            if col not in df.columns:
                df[col] = val
                
        # 0. Obtener Datos Aumentados para mostrar en UI
        augmented_df = self.preprocessor._augment_data(df)
        steps_run = int(augmented_df['Steps_Run'].iloc[0])
        time_taken = float(augmented_df['Time_Taken'].iloc[0])
                
        # 1. Transformación (Aumentación y Feature Engineering)
        X = self.preprocessor.transform(df)
        
        # 2. Asignación de Clúster
        cluster = self.clustering_model.predict(X)[0]
        
        # 3. Inyección del Clúster como Feature para el clasificador supervisado
        X['Cluster'] = cluster
        
        # 4. Inferencia Dual
        probs = self.classifier_model.predict_proba(X)[0]
        
        # Las clases son 0: Gol, 1: Atajada, 2: Fallo
        prob_gol = float(probs[0] if len(probs) > 0 else 0)
        prob_atajada = float(probs[1] if len(probs) > 1 else 0)
        prob_fallo = float(probs[2] if len(probs) > 2 else 0)
        
        return {
            "probabilities": {
                "Gol": prob_gol,
                "Atajada": prob_atajada,
                "Fallo": prob_fallo
            },
            "cluster_assigned": int(cluster),
            "steps_run": steps_run,
            "time_taken": time_taken
        }
