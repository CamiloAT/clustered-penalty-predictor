import os
import sys
import joblib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_data
from src.preprocessor import PenaltyPreprocessor, split_data

def run_preprocessing():
    print("Ejecutando pipeline de preprocesamiento...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 1. Cargar datos
    print("Cargando datos...")
    df = load_data(os.path.join(base_dir, 'data', 'WorldCupShootouts.csv'))

    # Limpiar mayúsculas/minúsculas
    df['Keeper'] = df['Keeper'].astype(str).str.upper()
    df['Foot'] = df['Foot'].astype(str).str.upper()

    # 2. Preprocesamiento (Feature Engineering + Encoding)
    print("Aplicando PenaltyPreprocessor...")
    preprocessor = PenaltyPreprocessor()
    X, y = preprocessor.fit_transform(df)

    # 3. Split 70/15/15
    print("Dividiendo datos (70% train, 15% val, 15% test)...")
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = split_data(X, y)

    # 4. Guardar splits y preprocessor
    output_dir = os.path.join(base_dir, 'outputs', 'processed')
    os.makedirs(output_dir, exist_ok=True)

    X_train.to_pickle(os.path.join(output_dir, 'X_train.pkl'))
    X_val.to_pickle(os.path.join(output_dir, 'X_val.pkl'))
    X_test.to_pickle(os.path.join(output_dir, 'X_test.pkl'))
    y_train.to_pickle(os.path.join(output_dir, 'y_train.pkl'))
    y_val.to_pickle(os.path.join(output_dir, 'y_val.pkl'))
    y_test.to_pickle(os.path.join(output_dir, 'y_test.pkl'))
    joblib.dump(preprocessor, os.path.join(output_dir, 'preprocessor.pkl'))

    print(f"Datos preprocesados guardados en {output_dir}")
    print(f"Train: {len(X_train)} | Val: {len(X_val)} | Test: {len(X_test)}")

if __name__ == "__main__":
    run_preprocessing()
