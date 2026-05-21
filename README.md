# Clustered Penalty Predictor

Sistema predictivo y analítico para cobros de penales de fútbol, utilizando Machine Learning (Clustering + Clasificación).

## Estructura del Proyecto

* **`data/`**: Datos crudos (`WorldCupShootouts.csv`).
* **`src/`**: Lógica core (Data Loader, Preprocesador, Clustering, Clasificador, Evaluador, Predictor).
* **`pipelines/`**: Scripts secuenciales para EDA, Preprocesamiento, Entrenamiento y Evaluación.
* **`models/`**: Modelos serializados (`.pkl`).
* **`api/`**: Interfaz REST usando FastAPI.
* **`frontend/`**: Interfaz visual (HTML/CSS/JS) llamativa orientada a fútbol.
* **`outputs/`**: Gráficos generados y reportes.

## Instalación

1. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso de la Interfaz

Abre `frontend/index.html` en cualquier navegador web moderno para visualizar la herramienta predictiva.

## Uso del API

Ejecutar el servidor local:
```bash
uvicorn api.main:app --reload
```
Luego visita `http://127.0.0.1:8000/docs` para ver la documentación interactiva (Swagger).
