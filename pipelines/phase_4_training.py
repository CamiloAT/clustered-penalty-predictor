import os
import sys
import joblib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_data
from src.preprocessor import PenaltyPreprocessor, split_data
from src.clustering import PenaltyClustering
from src.classifier import PenaltyClassifier
from src.evaluator import evaluate_clustering, evaluate_classifier

def run_training():
    print("Iniciando fase de entrenamiento y construcción de pipeline...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Cargar datos
    print("Cargando datos...")
    df = load_data(os.path.join(base_dir, 'data', 'WorldCupShootouts.csv'))
    
    # Limpiar mayúsculas/minúsculas en 'Keeper' y 'Foot'
    df['Keeper'] = df['Keeper'].astype(str).str.upper()
    df['Foot'] = df['Foot'].astype(str).str.upper()
    
    # 2. Preprocesamiento (Aumentación y Feature Engineering)
    print("Preprocesando datos (Data Augmentation)...")
    preprocessor = PenaltyPreprocessor()
    X, y = preprocessor.fit_transform(df)
    
    # Dividir
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = split_data(X, y)
    
    # 3. Clustering
    print("Entrenando clustering K-Means...")
    clustering = PenaltyClustering(n_clusters=4)
    clustering.fit(X_train)
    
    # Inyectar cluster
    X_train = X_train.copy()
    X_train['Cluster'] = clustering.predict(X_train)
    
    X_test = X_test.copy()
    X_test['Cluster'] = clustering.predict(X_test)
    
    # 4. Clasificador
    print("Entrenando clasificador Random Forest...")
    classifier = PenaltyClassifier()
    classifier.fit(X_train, y_train)
    
    # Guardar Modelos
    print("Guardando artefactos en la carpeta models/...")
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    joblib.dump(preprocessor, os.path.join(models_dir, 'preprocessor.pkl'))
    clustering.save_model(os.path.join(models_dir, 'kmeans_model.pkl'))
    classifier.save_model(os.path.join(models_dir, 'classifier_model.pkl'))
    
    # Evaluar rápido y exportar matrices
    print("Exportando matrices a outputs/evaluation_plots/...")
    plots_dir = os.path.join(base_dir, 'outputs', 'evaluation_plots')
    os.makedirs(plots_dir, exist_ok=True)
    y_pred = classifier.predict(X_test)
    evaluate_classifier(y_test, y_pred, output_dir=plots_dir)
    evaluate_clustering(X_train, X_train['Cluster'].values, output_dir=plots_dir)
    
    print("¡Entrenamiento finalizado con éxito!")

if __name__ == "__main__":
    run_training()
