from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def evaluate_clustering(X: pd.DataFrame, labels: np.ndarray, max_clusters=10, output_dir="."):
    """Calcula el Índice de Silueta y genera la gráfica del Método del Codo."""
    sil_score = silhouette_score(X, labels)
    
    inertias = []
    K_range = range(2, max_clusters + 1)
    for k in K_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X)
        inertias.append(km.inertia_)
        
    plt.figure(figsize=(8,5))
    plt.plot(K_range, inertias, marker='o', linestyle='--', color='#00d26a')
    plt.title('Método del Codo para KMeans')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Inercia')
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{output_dir}/elbow_method.png")
    plt.close()
    
    return {"silhouette_score": sil_score}

def evaluate_classifier(y_true, y_pred, output_dir="."):
    """Genera reportes técnicos y matriz de confusión."""
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='weighted')
    
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1, 2])
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
                xticklabels=['Gol', 'Atajada', 'Fallo'], 
                yticklabels=['Gol', 'Atajada', 'Fallo'])
    plt.title('Matriz de Confusión - Multiclase')
    plt.ylabel('Etiqueta Real')
    plt.xlabel('Predicción del Modelo')
    plt.savefig(f"{output_dir}/confusion_matrix.png")
    plt.close()
    
    return {"accuracy": acc, "f1_score": f1}
