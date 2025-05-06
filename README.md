<img src="https://www.repsol.com/content/dam/repsol-corporate/es/energia-e-innovacion/robot-machine-learning.jpg.transform/rp-rendition-sm/image.jpg" alt="Imagen de Machine Learning" width="700"/>

# 👨‍🎓 Estimación de Calificaciones y Predicción de Aprobación de Estudiantes

Este proyecto tiene como objetivo desarrollar dos modelos de Machine Learning para predecir el rendimiento académico de los estudiantes. Los modelos son:

1. **Modelo de predicción de calificaciones**: Predice la nota final de un estudiante.
2. **Modelo de predicción de aprobación**: Predice si un estudiante aprobará el curso (nota > 60).

---

## 📝 Descripción del Proyecto

Trabajamos con un conjunto de datos que contiene información académica y personal de estudiantes. El proyecto está dividido en las siguientes etapas:

1. **Limpieza de datos**
    Cargar el dataset, entender los datos y corregir todos los errores.

2. **Análisis Exploratorio de Datos (EDA)**  
   Identificación de patrones y relaciones.

3. **Preprocesamiento de Datos**  
   Codificación de variables categóricas y escalado de variables numéricas.

4. **Entrenamiento de Modelos**  
   Entrenar diferentes modelos, evaluarlos y afinar los mejores 

5. **Implementación con FastAPI**  
   Exposición de ambos modelos como una API accesible mediante peticiones HTTP POST.

6. **Dockerización del Proyecto**  
   El proyecto se ha dockerizado para facilitar su despliegue y portabilidad en cualquier entorno.

---

## 📂 Estructura del Proyecto


- **data/**
  - `dataset_estudiantes.csv`
  - `clean_dataset_estudiantes.csv`
  - `preprocessed_dataset.csv`

- **models/**
  - `regression_model.pkl`
  - `classification_model.pkl`
  - `standard_scaler.pkl`

- **notebooks/**
  - `01_Cleaning.ipynb`
  - `02_EDA.ipynb`
  - `03_Preprocessing.ipynb`
  - `04_Predictive_models.ipynb`

- `main.py`                     # API con FastAPI
- `functions.py`                # Funciones de preprocesamiento
- `requirements.txt`            # Dependencias del proyecto
- `Dockerfile`                  # Dockerfile para empaquetar la API
- `README.md`                   # Documentación del proyecto


---

## 📥 Requisitos

Este proyecto requiere las siguientes librerías de Python. Puedes instalar todas las dependencias necesarias ejecutando el siguiente comando:

``pip install -r requirements.txt``

Algunas de las dependencias principales incluyen:

- FastAPI: Framework para crear APIs rápidas.

- Uvicorn: Servidor ASGI para ejecutar FastAPI.

- pandas: Para la manipulación de datos.

- numpy: Para operaciones matemáticas.

- scikit-learn: Para entrenar y evaluar los modelos de Machine Learning.

- matplotlib y seaborn: Para visualización de datos.

---

## 🚀 Uso de la API

Una vez ejecutada la API, puedes acceder a:

- POST /predict/grade → Predice la calificación final del estudiante.

- POST /predict/pass → Predice si el estudiante aprueba o no.

## 🧪 Ejemplo de entrada JSON:

{
  "horas_estudio_semanal": 5,
  "nota_anterior": 65,
  "tasa_asistencia": 90,
  "horas_sueno": 7,
  "edad": 19,
  "nivel_dificultad": "medio",
  "tiene_tutor": "sí",
  "estilo_aprendizaje": "visual",
  "horario_estudio_preferido": "noche"
}

---

# 🐳 Docker

### Construcción de la imagen

docker build -t student-api .

### Ejecución del contenedor

docker run -p 8000:8000 student-api

### Acceso a la documentación

Una vez desplegado, accede a la documentación interactiva de la API en:
http://localhost:8000/docs

---

## 📊 Resultados y conclusiones

### Conclusiones Regresión:
El modelo Lasso ha mostrado un desempeño más equilibrado, con un R² cercano al 34-35% tanto en el conjunto de entrenamiento como en el de prueba. Esto indica que el modelo generaliza bien sin sobreajustarse. Además, Lasso presenta un menor error cuadrático medio (RMSE), lo que sugiere una mayor precisión en las predicciones.

Por estos motivos, se ha elegido el modelo Lasso como la opción más adecuada para este caso. Se realizará el entrenamiento final y se guardará el modelo.

### Conclusiones Finales Clasificación:
Aunque la precisión de la regresión logística es la más alta, esto puede ser engañoso si no consideramos otras métricas clave como el recall y el F1-Score. La precisión solo mide la proporción de predicciones correctas entre las predicciones positivas, pero no toma en cuenta los falsos negativos, es decir, las instancias que el modelo no predice correctamente.

El **Random Forest** ofrece un mejor equilibrio entre precisión y recall, lo cual lo convierte en la opción más robusta. Este modelo será guardado para su uso posterior.


## 📌 Próximos Pasos

- **Optimización de Modelos**: Mejorar el rendimiento de los modelos mediante técnicas como la selección de características, optimización de hiperparámetros y pruebas con otros algoritmos.
- **Ampliación del dataset**: Incluir más datos y/o características relevantes para mejorar la capacidad predictiva.


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.

## 👨‍💻 Autor

- Sergio Delgado
- sergiodelamp@gmail.com
- https://github.com/Sergiio02
