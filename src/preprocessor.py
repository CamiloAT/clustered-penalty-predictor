import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

class PenaltyPreprocessor:
    def __init__(self):
        self.team_effectiveness = {}
        self.keeper_save_rate = {}
        self.preprocessor = None
        
        self.categorical_features = ['Foot']
        self.numeric_features = [
            'Steps_Run', 'Time_Taken', 'Team_Effectiveness', 
            'Stress_Index', 'Penalty_Number'
        ]
        
    def _augment_data(self, df: pd.DataFrame) -> pd.DataFrame:
        data = df.copy()
        
        # Eliminar NaN para variables de contexto
        data['Elimination'] = data['Elimination'].fillna(0).astype(int)
        data['Penalty_Number'] = data['Penalty_Number'].fillna(1).astype(int)
        
        # Feature Engineering: Indicador compuesto de estrés
        data['Stress_Index'] = data['Penalty_Number'] * (data['Elimination'] + 1)
        
        # Data Augmentation a): "Steps_Run" (correlacionado con Foot y Estrés)
        np.random.seed(42)
        base_steps = np.where(data['Foot'] == 'L', 5, 6)
        stress_modifier = (data['Stress_Index'] / (data['Stress_Index'].max() + 1e-9) * 2).astype(int)
        data['Steps_Run'] = base_steps + stress_modifier + np.random.randint(-1, 2, size=len(data))
        
        # Data Augmentation b): "Time_Taken" (incrementado bajo presión)
        base_time = np.random.uniform(3.0, 5.0, size=len(data))
        high_pressure_mask = (data['Elimination'] == 1) | (data['Penalty_Number'] > 5)
        data['Time_Taken'] = base_time + np.where(high_pressure_mask, np.random.uniform(2.0, 4.0, size=len(data)), 0)
        
        return data
        
    def _feature_engineering_fit(self, df: pd.DataFrame):
        # Tasa de efectividad histórica de goles por 'Team'
        team_stats = df.groupby('Team')['Goal'].mean()
        self.team_effectiveness = team_stats.to_dict()
        
        # Tasa de atajadas históricas del portero ('Keeper') cuando Goal=0 y OnTarget=1
        saves_mask = (df['Goal'] == 0) & (df['OnTarget'] == 1)
        keeper_shots = df.groupby('Keeper').size()
        keeper_saves = df[saves_mask].groupby('Keeper').size()
        self.keeper_save_rate = (keeper_saves / keeper_shots).fillna(0).to_dict()
        
    def _feature_engineering_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        data = df.copy()
        global_team_mean = np.mean(list(self.team_effectiveness.values())) if self.team_effectiveness else 0.5
        global_keeper_mean = np.mean(list(self.keeper_save_rate.values())) if self.keeper_save_rate else 0.2
        
        data['Team_Effectiveness'] = data['Team'].map(self.team_effectiveness).fillna(global_team_mean)
        data['Keeper_Save_Rate'] = data['Keeper'].map(self.keeper_save_rate).fillna(global_keeper_mean)
        return data

    def _create_multiclass_target(self, df: pd.DataFrame) -> pd.Series:
        # 0: Gol, 1: Atajada, 2: Fallo desviado
        conditions = [
            (df['Goal'] == 1),
            (df['Goal'] == 0) & (df['OnTarget'] == 1),
            (df['Goal'] == 0) & (df['OnTarget'] == 0)
        ]
        choices = [0, 1, 2]
        return pd.Series(np.select(conditions, choices, default=2), index=df.index)

    def fit_transform(self, df: pd.DataFrame):
        data = self._augment_data(df)
        self._feature_engineering_fit(data)
        data = self._feature_engineering_transform(data)
        
        y = self._create_multiclass_target(data)
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numeric_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), self.categorical_features)
            ])
            
        features_to_transform = data[self.numeric_features + self.categorical_features]
        X_transformed = self.preprocessor.fit_transform(features_to_transform)
        
        cat_names = self.preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features)
        feature_names = self.numeric_features + list(cat_names)
        
        X_df = pd.DataFrame(X_transformed, columns=feature_names, index=data.index)
        return X_df, y
        
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        data = self._augment_data(df)
        data = self._feature_engineering_transform(data)
        features_to_transform = data[self.numeric_features + self.categorical_features]
        X_transformed = self.preprocessor.transform(features_to_transform)
        
        cat_names = self.preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features)
        feature_names = self.numeric_features + list(cat_names)
        
        return pd.DataFrame(X_transformed, columns=feature_names, index=data.index)

def split_data(X, y):
    """Divide estrictamente en 70% train, 15% val, 15% test"""
    # Manejar caso de pocas muestras en algunas clases con stratify si es posible
    try:
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp)
    except ValueError:
        # Fallback sin stratify si hay clases con 1 sola muestra
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)
        
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)
