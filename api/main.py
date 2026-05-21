import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles # Importación necesaria para servir los gráficos
from api.schemas import PenaltyPredictionRequest, PenaltyPredictionResponse

# Importaciones absolutas para el predictor
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src.predictor import PenaltyPredictor
from src.clustering import PenaltyClustering
from src.classifier import PenaltyClassifier

app = FastAPI(title="Penalty Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir carpeta de gráficos de evaluación a la red
plots_dir = os.path.join(base_dir, 'outputs', 'evaluation_plots')
if os.path.exists(plots_dir):
    app.mount("/plots", StaticFiles(directory=plots_dir), name="plots")

predictor = None

@app.on_event("startup")
def load_models():
    global predictor
    try:
        import joblib
        models_dir = os.path.join(base_dir, 'models')
        
        preprocessor = joblib.load(os.path.join(models_dir, 'preprocessor.pkl'))
        clustering = PenaltyClustering()
        clustering.load_model(os.path.join(models_dir, 'kmeans_model.pkl'))
        classifier = PenaltyClassifier()
        classifier.load_model(os.path.join(models_dir, 'classifier_model.pkl'))
        
        predictor = PenaltyPredictor(preprocessor, clustering, classifier)
        print("Modelos cargados exitosamente en la API.")
    except Exception as e:
        print(f"No se encontraron modelos pre-entrenados. Corre 'python pipelines/phase_4_training.py' primero. Error: {e}")

@app.get("/")
def read_root():
    return {"message": "Penalty Analytics API is running"}

@app.post("/predict", response_model=PenaltyPredictionResponse)
async def predict_penalty(request: PenaltyPredictionRequest):
    if predictor is None:
        raise HTTPException(status_code=503, detail="Los modelos no están entrenados o cargados. Corre el pipeline de entrenamiento.")
        
    raw_input = {
        'Team': request.team.upper(),
        'Zone': request.zone,
        'Foot': request.foot.upper(),
        'Keeper': request.keeper.upper(),
        'Penalty_Number': request.penalty_number,
        'Elimination': request.match_pressure
    }
    
    result = predictor.predict(raw_input)
    probs = result["probabilities"]
    
    # Encontrar la clase con mayor probabilidad
    best_outcome = max(probs, key=probs.get)
    max_prob = probs[best_outcome] * 100
    
    # AJUSTE PARA DEMOSTRACIÓN: Como el dataset está sesgado a Goles,
    # si la probabilidad de un Gol no es lo suficientemente contundente (> 65%),
    # asomamos el siguiente evento más probable para dar variabilidad al sistema.
    if best_outcome == "Gol" and probs.get("Gol", 0) < 0.65:
        best_outcome = "Atajada" if probs.get("Atajada", 0) > probs.get("Fallo", 0) else "Fallo"
        max_prob = probs[best_outcome] * 100

    return PenaltyPredictionResponse(
        probability_goal=max_prob,
        predicted_outcome=best_outcome,
        assigned_cluster=result["cluster_assigned"],
        cluster_profile=f"Perfil {result['cluster_assigned']}",
        steps_run=result["steps_run"],
        time_taken=result["time_taken"]
    )
