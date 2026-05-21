import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def run_eda(data_path: str, output_dir: str):
    print("Iniciando EDA...")
    df = pd.read_csv(data_path)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Ejemplo de gráfico
    plt.figure(figsize=(8,6))
    sns.countplot(x='Zone', hue='Goal', data=df)
    plt.title('Goles por Zona')
    plt.savefig(Path(output_dir) / 'goles_por_zona.png')
    plt.close()
    print(f"Gráficos guardados en {output_dir}")

if __name__ == "__main__":
    run_eda("../data/WorldCupShootouts.csv", "../outputs/eda_plots")
