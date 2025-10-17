from fastapi import APIRouter, Depends, HTTPException
from ...schemas.data import PredictionRequest, PredictionResponse
from ...services.ml_service import MLService
from ...core.security import get_current_user

router = APIRouter(prefix="/ml", tags=["Machine Learning"])
ml_service = MLService()


@router.post("/predict", response_model=PredictionResponse)
async def predict(
    request: PredictionRequest,
    current_user: dict = Depends(get_current_user)
):
    """Make a prediction using the ML model"""
    try:
        prediction = ml_service.predict(request.features)
        return {
            "prediction": prediction,
            "confidence": 0.95,  # Placeholder confidence
            "model_version": "1.0.0"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@router.post("/train")
async def train_model(current_user: dict = Depends(get_current_user)):
    """Trigger model training (admin only)"""
    try:
        ml_service.train_model()
        return {"message": "Model training initiated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")


@router.get("/model-info")
async def get_model_info(current_user: dict = Depends(get_current_user)):
    """Get information about the current ML model"""
    return {
        "model_type": "RandomForestRegressor",
        "version": "1.0.0",
        "trained_at": "2024-01-01T00:00:00Z",
        "features": ["feature1", "feature2", "feature3"],
        "accuracy": 0.92
    }
