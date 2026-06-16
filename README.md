# Clustered Penalty Predictor

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

A Machine Learning pipeline that predicts penalty kick outcomes in football and discovers hidden behavioral profiles among kickers using supervised classification and unsupervised clustering.

---

## Main Features

- **Dual-Model Pipeline** — Combines Random Forest classification with K-Means clustering for richer predictions.
- **Kicker Profile Discovery** — Identifies 4 distinct behavioral profiles (Cold, Power, Pressure, Inexperienced) from historical data.
- **Cluster-Enhanced Predictions** — Injects the discovered cluster as an additional feature into the classifier, boosting accuracy.
- **Interactive Web Interface** — Single-page glassmorphism UI with a 3-step wizard for selecting goal zones, keeper position, and match context.
- **Real-Time Animations** — Full-screen animated overlays for Goal, Save, and Miss outcomes.
- **Evaluation Dashboard** — Displays confusion matrix, elbow method, feature importance, and per-class metrics via modal.
- **Production-Ready API** — FastAPI backend with pre-trained models, deployed on Render.com.

---

## Pages & Views

| View | Description |
|---|---|
| **Prediction Wizard** | 3-step form: select goal zone (9-grid), keeper dive zone (9-grid), and match context (team, foot, penalty number, pressure). |
| **Result Panel** | Displays predicted outcome with circular probability chart, cluster assignment, and profile name. |
| **Metrics Modal** | Shows 4 evaluation plots: Confusion Matrix, Elbow Method, Feature Importance, Per-Class Metrics. |
| **Cluster Info Modal** | Presents 4 cluster profile cards with descriptions and visual identities. |

---

## Execution and Development Guide

### 1. Clone the repository

```bash
git clone https://github.com/CamiloAT/clustered-penalty-predictor.git
cd clustered-penalty-predictor
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

### 3. Run the ML training pipeline (optional)

```bash
# Run all 5 phases sequentially
python pipelines/phase_1_eda.py
python pipelines/phase_2_preprocessing.py
python pipelines/phase_3_clustering.py
python pipelines/phase_4_training.py
python pipelines/phase_5_evaluation.py
```

> **Note:** The `models/` directory already contains pre-trained `.pkl` files. You only need to run the pipeline if you want to retrain or explore the data.

### 4. Start the API backend

```bash
uvicorn api.main:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`. Test it at `http://127.0.0.1:8000/docs`.

### 5. Open the frontend

Open `frontend/index.html` directly in your browser. It automatically connects to `http://127.0.0.1:8000` when running on localhost.

> **Note:** In production, the frontend is served from Vercel and the API runs on Render.com. No local setup needed for the live version at https://clustered-penalty-predictor.vercel.app/.

---

## Project Structure

```text
clustered-penalty-predictor/
├── api/                              # FastAPI backend
│   ├── main.py                       #   API endpoints and model loading
│   └── schemas.py                    #   Pydantic request/response models
│
├── src/                              # Core ML modules
│   ├── data_loader.py                #   CSV data loading with validation
│   ├── preprocessor.py               #   Feature engineering, augmentation, encoding
│   ├── clustering.py                 #   K-Means clustering (4 clusters)
│   ├── classifier.py                 #   Random Forest classifier (multiclass)
│   ├── predictor.py                  #   Integrated inference pipeline
│   └── evaluator.py                  #   Metrics, plots, evaluation utilities
│
├── pipelines/                        # Executable training phases (CRISP-DM)
│   ├── phase_1_eda.py                #   Exploratory Data Analysis
│   ├── phase_2_preprocessing.py      #   Data loading, augmentation, splitting
│   ├── phase_3_clustering.py         #   K-Means training and evaluation
│   ├── phase_4_training.py           #   Full pipeline: preprocess → cluster → train
│   └── phase_5_evaluation.py         #   Load models, evaluate, generate plots
│
├── models/                           # Serialized ML artifacts (.pkl)
│   ├── preprocessor.pkl              #   Fitted ColumnTransformer
│   ├── kmeans_model.pkl              #   Trained K-Means model
│   └── classifier_model.pkl          #   Trained Random Forest model
│
├── data/
│   └── WorldCupShootouts.csv         # Historical World Cup penalty shootout data
│
├── outputs/
│   └── evaluation_plots/             # Generated evaluation visualizations
│
├── frontend/                         # Static web interface
│   ├── index.html                    #   Single-page app
│   ├── styles.css                    #   Glassmorphism UI
│   ├── script.js                     #   Frontend logic and API calls
│   ├── logo.png                      #   App logo
│   └── bg.png                        #   Stadium background image
│
├── requirements.txt                  # Python dependencies
├── vercel.json                       # Vercel deployment config
└── project.md                        # Full academic report
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **API Framework** | FastAPI + Uvicorn |
| **ML Algorithms** | Random Forest (scikit-learn), K-Means (scikit-learn) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Model Serialization** | Joblib |
| **Schema Validation** | Pydantic v2 |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JavaScript |
| **Frontend Hosting** | Vercel |
| **Backend Hosting** | Render.com |
| **Dataset** | FIFA World Cup Penalty Shootouts (Kaggle) |

---

## Authors

| Name | GitHub |
|---|---|
| **Camilo Andres Arias Tenjo** | [@CamiloAT](https://github.com/CamiloAT) |
| **Diego Fernando Aguirre Tenjo** | [@elcokiin](https://github.com/elcokiin) |

*Applied Machine Learning*
