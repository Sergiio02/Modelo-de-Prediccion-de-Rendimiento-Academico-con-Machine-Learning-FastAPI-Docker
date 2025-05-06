import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

# Cargar el scaler entrenado (se guarda durante el entrenamiento)
# Si no existe, se creará uno nuevo (pero lo ideal es usar el del entrenamiento)
try:
    scaler = joblib.load("models/standard_scaler.pkl")
except:
    scaler = StandardScaler()

# Función para hacer el One-Hot Encoding de las columnas categóricas
def one_hot_encoding(df):
    # Definir todas las posibles categorías para asegurar que siempre tendremos las mismas columnas
    tutor_categories = ['sí', 'no']
    estilo_categories = ['auditivo', 'visual', 'kinestésico', 'lectura/escritura', 'desconocido']
    horario_categories = ['mañana', 'tarde', 'noche', 'desconocido']
    
    # Hacer one-hot encoding con todas las categorías posibles
    df = pd.get_dummies(df, columns=['tiene_tutor'], prefix=['tiene_tutor'])
    df = pd.get_dummies(df, columns=['estilo_aprendizaje'], prefix=['estilo_aprendizaje'])
    df = pd.get_dummies(df, columns=['horario_estudio_preferido'], prefix=['horario_estudio_preferido'])
    
    # Asegurar que todas las columnas esperadas estén presentes
    # Para 'tiene_tutor'
    for cat in tutor_categories:
        col_name = f'tiene_tutor_{cat}'
        if col_name not in df.columns:
            df[col_name] = 0
    
    # Para 'estilo_aprendizaje'
    for cat in estilo_categories:
        col_name = f'estilo_aprendizaje_{cat}'
        if col_name not in df.columns:
            df[col_name] = 0
    
    # Para 'horario_estudio_preferido'
    for cat in horario_categories:
        col_name = f'horario_estudio_preferido_{cat}'
        if col_name not in df.columns:
            df[col_name] = 0
    
    # Convertir las columnas one-hot a enteros (0 y 1)
    dummy_columns = [col for col in df.columns if col.startswith(('tiene_tutor_', 'estilo_aprendizaje_', 'horario_estudio_preferido_'))]
    df[dummy_columns] = df[dummy_columns].astype(int)
    
    return df

# Función para hacer el Ordinal Encoding de la columna nivel_dificultad
def ordinal_encoding(df):
    encoder = OrdinalEncoder(categories=[['fácil', 'medio', 'difícil']])
    df["nivel_dificultad"] = encoder.fit_transform(df[['nivel_dificultad']])
    return df

# Función para escalar las características numéricas
def scale_numerical_features(df):
    num_cols_to_scale = ["horas_estudio_semanal", "nota_anterior", "tasa_asistencia", "horas_sueno", "edad"]
    
    # Verificar si todas las columnas numéricas existen en el dataframe
    for col in num_cols_to_scale:
        if col not in df.columns:
            raise ValueError(f"La columna {col} no está presente en el dataframe")
    
    # Usar transform en lugar de fit_transform para aplicar la misma transformación que en entrenamiento
    df[num_cols_to_scale] = scaler.transform(df[num_cols_to_scale])
    return df