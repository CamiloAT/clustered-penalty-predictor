import pandas as pd
from pathlib import Path

def load_data(filepath: str) -> pd.DataFrame:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {filepath}")
    
    df = pd.read_csv(path)
    
    required_columns = ['Game_id', 'Team', 'Zone', 'Foot', 'Keeper', 'OnTarget', 'Goal', 'Penalty_Number', 'Elimination']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Falta la columna requerida en el CSV: {col}")
    
    return df
