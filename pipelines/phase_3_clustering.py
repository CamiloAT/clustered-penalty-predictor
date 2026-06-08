import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_data
from src.preprocessor import PenaltyPreprocessor, split_data
from src.clustering import PenaltyClustering
from src.evaluator import evaluate_clustering

def run_clustering():
    print("Ejecutando pipeline de clustering K-Means...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 1. Cargar y preprocesar datos
    print("Cargando y preprocesando datos...")
    df = load_data(os.path.join(base_dir, 'data', 'WorldCupShootouts.csv'))
    df['Keeper'] = df['Keeper'].astype(str).str.upper()
    df['Foot'] = df['Foot'].astype(str).str.upper()

    preprocessor = PenaltyPreprocessor()
    X, y = preprocessor.fit_transform(df)
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = split_data(X, y)

    # 2. Entrenar clustering
    print("Entrenando K-Means con 4 clusters...")
    clustering = PenaltyClustering(n_clusters=4)
    clustering.fit(X_train)

    # 3. Predecir etiquetas
    train_labels = clustering.predict(X_train)

    # 4. Evaluar y exportar gráfica del codo
    print("Evaluando clustering y generando gráficas...")
    plots_dir = os.path.join(base_dir, 'outputs', 'evaluation_plots')
    os.makedirs(plots_dir, exist_ok=True)
    metrics = evaluate_clustering(X_train, train_labels, output_dir=plots_dir)
    print(f"Silhouette Score: {metrics['silhouette_score']:.4f}")

    # 5. Guardar modelo
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)
    clustering.save_model(os.path.join(models_dir, 'kmeans_model.pkl'))
    print(f"Modelo guardado en {models_dir}")

if __name__ == "__main__":
    run_clustering()
