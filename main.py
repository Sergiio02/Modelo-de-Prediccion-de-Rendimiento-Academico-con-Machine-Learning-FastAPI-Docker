from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import logging
from functions import one_hot_encoding, ordinal_encoding, scale_numerical_features

# Configurar logging para depuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar modelos
try:
    regression_model = joblib.load("models/regression_model.pkl")
    classification_model = joblib.load("models/classification_model.pkl")
    logger.info("Modelos cargados correctamente")
except Exception as e:
    logger.error(f"Error al cargar los modelos: {e}")
    raise

app = FastAPI(title="Student Grade Prediction API")

class StudentInput(BaseModel):
    horas_estudio_semanal: float
    nota_anterior: float
    tasa_asistencia: float
    horas_sueno: float
    edad: float
    nivel_dificultad: str  # "fácil", "medio", "difícil"
    tiene_tutor: str  # "sí" o "no"
    estilo_aprendizaje: str  # auditivo, visual, kinestésico, lectura/escritura, desconocido
    horario_estudio_preferido: str  # mañana, tarde, noche, desconocido

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de predicción de estudiantes"}

@app.post("/predict/grade")
def predict_grade(data: StudentInput):
    try:
        # Convertir el input a un dataframe
        df = pd.DataFrame([data.dict()])
        logger.info(f"Datos recibidos: {df.to_dict()}")
        
        # Aplicar One-Hot Encoding
        df = one_hot_encoding(df)
        logger.info(f"Después de one-hot encoding, columnas: {df.columns.tolist()}")
        
        # Aplicar Ordinal Encoding
        df = ordinal_encoding(df)
        logger.info(f"Después de ordinal encoding, nivel_dificultad: {df['nivel_dificultad'].values}")
        
        # Aplicar escalado a las características numéricas
        df = scale_numerical_features(df)
        logger.info(f"Después de escalar, primeras columnas numéricas: {df[['horas_estudio_semanal', 'nota_anterior']].head()}")

        # Verificar número de features
        logger.info(f"Número de características: {df.shape[1]}")
        
        # Hacer predicción
        features = df.values  # Convertir el DataFrame a un array de características
        prediction = regression_model.predict(features)[0]
        
        # Limitar la nota entre 0 y 100
        prediction = max(0, min(100, prediction))
        
        return {"predicted_grade": round(prediction, 2)}
    
    except Exception as e:
        logger.error(f"Error en la predicción: {e}")
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {e}")

@app.post("/predict/pass")
def predict_pass(data: StudentInput):
    try:
        # Convertir el input a un dataframe
        df = pd.DataFrame([data.dict()])
        logger.info(f"Datos recibidos: {df.to_dict()}")

        # Aplicar One-Hot Encoding
        df = one_hot_encoding(df)
        logger.info(f"Después de one-hot encoding, columnas: {df.columns.tolist()}")

        # Aplicar Ordinal Encoding
        df = ordinal_encoding(df)
        logger.info(f"Después de ordinal encoding, nivel_dificultad: {df['nivel_dificultad'].values}")

        # Aplicar escalado a las características numéricas
        df = scale_numerical_features(df)
        logger.info(f"Después de escalar, primeras columnas numéricas: {df[['horas_estudio_semanal', 'nota_anterior']].head()}")

        # Verificar número de features
        logger.info(f"Número de características: {df.shape[1]}")

        # Hacer predicción
        features = df.values  # Convertir el DataFrame a un array de características
        prediction = classification_model.predict(features)[0]
        result = "Aprobado" if prediction == 1 else "Suspendido"
        return {"prediction": result, "class": int(prediction)}
    
    except Exception as e:
        logger.error(f"Error en la predicción: {e}")
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {e}")