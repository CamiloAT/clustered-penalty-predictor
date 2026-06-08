import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.clustering import PenaltyClustering
from src.evaluator import evaluate_clustering

def run_clustering():
    print("Ejecutando pipeline de clustering K-Means...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 1. Cargar datos preprocesados
    processed_dir = os.path.join(base_dir, 'outputs', 'processed')
    X_train = pd.read_pickle(os.path.join(processed_dir, 'X_train.pkl'))

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
