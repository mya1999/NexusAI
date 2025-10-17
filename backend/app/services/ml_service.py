import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os
from typing import List


class MLService:
    """Machine Learning service for predictions"""
    
    def __init__(self):
        self.model_path = "/app/ml_models/model.pkl"
        self.model = None
        self.load_model()
    
    def load_model(self):
        """Load the trained model or create a new one"""
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
                print("Model loaded successfully")
            except Exception as e:
                print(f"Error loading model: {e}")
                self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        else:
            print("No existing model found, creating new one")
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            # Train with dummy data for initialization
            X = np.random.rand(100, 3)
            y = np.random.rand(100)
            self.model.fit(X, y)
            self.save_model()
    
    def save_model(self):
        """Save the trained model"""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print("Model saved successfully")
    
    def predict(self, features: List[float]) -> float:
        """Make a prediction"""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        features_array = np.array(features).reshape(1, -1)
        prediction = self.model.predict(features_array)
        return float(prediction[0])
    
    def train_model(self):
        """Train the model with new data"""
        # Generate synthetic training data for demonstration
        X = np.random.rand(1000, 3)
        y = X[:, 0] * 2 + X[:, 1] * 3 - X[:, 2] + np.random.randn(1000) * 0.1
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        score = self.model.score(X_test, y_test)
        print(f"Model trained with R² score: {score}")
        
        self.save_model()
        return score
