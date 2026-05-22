# Clustered Penalty Predictor ⚽

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

A modern, interactive, and complete Machine Learning pipeline for predicting soccer penalty outcomes using historical data from the World Cup. This project implements a dual-modeling approach: K-Means clustering for profiling and Random Forest classification for outcome prediction.

---

## Project Information

**Course:** ELECTIVA II - MACHINE LEARNING APLICADO (8108277)
**Group** (1 - 0)  
**Credits:** 3
**Professor:** VIVIANA ALEXANDRA VILLANUEVA CIPAGAUTA  

### Team Members
| Name | Code |
| :--- | :--- |
| **Diego Fernando Aguirre Tenjo** | 202212048 |
| **Camilo Andrés Arias Tenjo** | 202210549 |

---

## Main Features

### Data Preprocessing & Augmentation
* **Feature Augmentation:** Algorithmic generation of `Steps_Run` and `Time_Taken` based on contextual data (pressure, foot) to simulate biomechanical variables.
* **Feature Engineering:** Calculation of historical success rates for both teams and goalkeepers.

### Dual Machine Learning Modeling
* **Unsupervised (K-Means):** Groups penalties into distinct profiles (clusters) representing different shooting styles.
* **Supervised (Random Forest):** Predicts the specific outcome (`Gol`, `Atajada`, `Fallo`) by injecting the computed cluster as a powerful predictive feature.

### Modern Interactive Interface (Frontend)
* Stunning dark-themed glassmorphism UI.
* Interactive 3x3 goal net to visually select the target zone (`Zone`).
* Breathtaking CSS animations for Goal (`¡GOLAZO!`) and Miss (`¡FALLO!`) outcomes.

---

## Execution and Development

1. **Create and Activate a Virtual Environment:**
   Run the following commands in the project root to isolate dependencies:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install required dependencies:**
   With the virtual environment activated, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API (Backend) in development mode:**
   Launch the FastAPI server that loads the trained `.pkl` models:
   ```bash
   uvicorn api.main:app --reload
   ```

4. **Open the Interface (Frontend):**
   Simply open the `frontend/index.html` file in your preferred web browser.

---

## Project Structure

```text
clustered-penalty-predictor/
│
├── data/                          ← Dataset original
│   └── WorldCupShootouts.csv      
│
├── src/                           ← Módulos genéricos del sistema
│   ├── data_loader.py             ← Carga y validación inicial
│   ├── preprocessor.py            ← Limpieza y Feature Engineering
│   ├── clustering.py              ← Modelado No Supervisado
│   ├── classifier.py              ← Modelado Supervisado
│   ├── predictor.py               ← Interfaz de inferencia final
│   ├── evaluator.py               ← Generación de métricas
│   └── __init__.py
│
├── pipelines/                     ← Scripts ejecutables por fase
│   ├── phase_1_eda.py             ← FASE 1: EDA
│   ├── phase_2_preprocessing.py   ← FASE 2: Preprocesamiento
│   ├── phase_3_clustering.py      ← FASE 3: Clustering (K-Means)
│   ├── phase_4_training.py        ← FASE 4: Random Forest
│   └── phase_5_evaluation.py      ← FASE 5: Evaluación
│
├── frontend/                      ← Aplicación Web (UI interactiva)
│   ├── index.html                 
│   ├── script.js                  
│   ├── styles.css                 
│   └── bg.png                     
│
├── models/                        ← Modelos serializados
│   ├── classifier_model.pkl       ← Random Forest .pkl
│   ├── kmeans_model.pkl           ← K-Means .pkl
│   └── preprocessor.pkl           ← Preprocesador general .pkl
│
├── api/                           ← FastAPI REST service
│   ├── main.py                    ← Endpoints del API REST
│   ├── schemas.py                 ← Esquemas Pydantic
│   └── __init__.py
│
├── outputs/                       
│   └── evaluation_plots/          
│       ├── confusion_matrix.png   
│       └── elbow_method.png       
│
├── requirements.txt               ← Dependencias
├── project.md                     
├── .gitignore                     
└── README.md                      
```

> [!NOTE]
> This project adheres to the CRISP-DM methodology, structurally separating data processing, modeling pipelines, the API exposure, and the frontend visualization.
