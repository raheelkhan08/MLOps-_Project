from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. API (Waiter) start kar rahe hain
app = FastAPI(title="Cyber Security Robot API")

# 2. Apna save kiya hua Robot aur Tool (Scaler) load kar rahe hain
model = joblib.load('smart_robot.pkl')
scaler = joblib.load('scaler_tool.pkl')

# 3. Format bata rahe hain ke kis shakal mein data aayega
class TrafficData(BaseModel):
    features: list[float]

# 4. Asal Kaam: Prediction karna
@app.post("/predict")
def predict_traffic(data: TrafficData):
    # Data ko API se uthaya
    input_data = np.array(data.features).reshape(1, -1)
    
    # Data ko normal range mein kiya (Scaling)
    scaled_data = scaler.transform(input_data)
    
    # Robot se pucha ke batao yeh kon hai?
    prediction = model.predict(scaled_data)
    
    # Jawab bheja
    if prediction[0] == 0:
        return {"Result": "Normal Traffic (Safe) ✅"}
    else:
        return {"Result": "Hacker Attack Detected! 🚨"}