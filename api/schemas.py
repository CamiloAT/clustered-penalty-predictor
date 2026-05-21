from pydantic import BaseModel, Field

class PenaltyPredictionRequest(BaseModel):
    team: str = Field(..., description="Equipo que cobra (Ej. ARG, FRA)")
    zone: int = Field(..., ge=1, le=9, description="Zona del arco (1-9)")
    foot: str = Field(..., description="Pie del cobrador (R o L)")
    keeper: str = Field(..., description="Movimiento del portero (L, C, R)")
    penalty_number: int = Field(..., description="Turno de penal en la tanda")
    match_pressure: int = Field(..., description="0 para fase de grupos, 1 para eliminatoria")

class PenaltyPredictionResponse(BaseModel):
    probability_goal: float
    predicted_outcome: str
    assigned_cluster: int
    cluster_profile: str
    steps_run: int
    time_taken: float
