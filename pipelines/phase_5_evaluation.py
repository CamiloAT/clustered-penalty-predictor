import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_data
from src.preprocessor import PenaltyPreprocessor, split_data
from src.evaluator import evaluate_classifier, evaluate_clustering
from src.clustering import PenaltyClustering
from src.classifier import PenaltyClassifier

def run_evaluation():
    print("Evaluando modelos y generando reportes...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plots_dir = os.path.join(base_dir, 'outputs', 'evaluation_plots')
    os.makedirs(plots_dir, exist_ok=True)

    # 1. Cargar modelos
    models_dir = os.path.join(base_dir, 'models')
    print("Cargando modelos desde models/...")
    classifier = PenaltyClassifier()
    classifier.load_model(os.path.join(models_dir, 'classifier_model.pkl'))

    clustering = PenaltyClustering()
    clustering.load_model(os.path.join(models_dir, 'kmeans_model.pkl'))

    # 2. Cargar y preprocesar datos para test
    print("Cargando y preprocesando datos...")
    df = load_data(os.path.join(base_dir, 'data', 'WorldCupShootouts.csv'))
    df['Keeper'] = df['Keeper'].astype(str).str.upper()
    df['Foot'] = df['Foot'].astype(str).str.upper()

    preprocessor = PenaltyPreprocessor()
    X, y = preprocessor.fit_transform(df)
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = split_data(X, y)

    # 3. Inyectar cluster en test
    X_test_clustered = X_test.copy()
    X_test_clustered['Cluster'] = clustering.predict(X_test)

    # 4. Evaluar clasificador
    print("Evaluando clasificador...")
    y_pred = classifier.predict(X_test_clustered)
    clf_metrics = evaluate_classifier(y_test, y_pred, output_dir=plots_dir)
    print(f"Accuracy: {clf_metrics['accuracy']:.4f} | F1-Score: {clf_metrics['f1_score']:.4f}")

    # 5. Evaluar clustering en train
    print("Evaluando clustering...")
    train_labels = clustering.predict(X_train)
    clust_metrics = evaluate_clustering(X_train, train_labels, output_dir=plots_dir)
    print(f"Silhouette Score: {clust_metrics['silhouette_score']:.4f}")

    print(f"Reportes y gráficas exportados a {plots_dir}")

if __name__ == "__main__":
    run_evaluation()
