from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
#import statsmodels.api as sm

# ----------------------------
# Cargar el modelo entrenado
# ----------------------------
model = joblib.load("model_medical_insurance.pkl")

# ----------------------------
# Crear la app FastAPI
# ----------------------------
app = FastAPI(title="API Predicción de Costos Médicos")

# ----------------------------
# Configurar CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringirlo a tu dominio de frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Definir el esquema de entrada
# ----------------------------
class InputData(BaseModel):
    age: float
    bmi: float
    smoker: int      # 0=no, 1=yes
    region: int      # 0=northeast, 1=northwest, 2=southeast, 3=southwest

# ----------------------------
# Endpoint de predicción
# ----------------------------
@app.post("/predict")
def predict(data: InputData):
    # Convertir los datos a DataFrame
    X_input = pd.DataFrame([data.dict()])

    # Realizar predicción
    prediction = model.predict(X_input)[0]

    return {
        "input_data": data.dict(),
        "prediction": float(prediction)
    }

# ----------------------------
# Ejemplo de inicio (opcional)
# ----------------------------
@app.get("/")
def root():
    return {
        "message": "API de Predicción de Costos Médicos lista 🚀",
        "example_input": {
            "age": 49,
            "sex": 0,
            "bmi": 29.9,
            "children": 0,
            "smoker": 0,
            "region": 1
        }
    }
