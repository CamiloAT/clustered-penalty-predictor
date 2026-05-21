from pydantic import BaseModel, Field

class PenaltyPredictionRequest(BaseModel):
    zone: int = Field(..., ge=1, le=9, description="Zona del arco (1-9)")
    foot: str = Field(..., description="Pie del cobrador (R o L)")
    keeper: str = Field(..., description="Movimiento del portero (L, C, R)")
    match_pressure: int = Field(..., description="0 para fase de grupos, 1 para eliminatoria")

class PenaltyPredictionResponse(BaseModel):
    probability_goal: float
    predicted_outcome: str
    assigned_cluster: int
    cluster_profile: str
