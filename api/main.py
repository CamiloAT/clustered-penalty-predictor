from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import PenaltyPredictionRequest, PenaltyPredictionResponse

app = FastAPI(title="Penalty Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Penalty Analytics API is running"}

@app.post("/predict", response_model=PenaltyPredictionResponse)
async def predict_penalty(request: PenaltyPredictionRequest):
    # TODO: Integrar con src.predictor (Machine Learning Model)
    # Respuesta simulada por ahora
    return PenaltyPredictionResponse(
        probability_goal=78.5,
        predicted_outcome="GOL",
        assigned_cluster=2,
        cluster_profile="Tiro Seguro y Potente"
    )
