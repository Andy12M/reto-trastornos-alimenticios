# reto-trastornos-alimenticios
# Detección de TCA en Tweets (NLP)

# Autores
* Andrea Doce Murillo
* Sandra Paulina Herrera Rebolledo
* Ian Alexei Mtz. Armendáriz


# Descripción del proyecto
Herramienta basada en NLP para detectar señales de trastornos de la conducta alimentaria (TCA) en tweets, clasificándolos como TCA o No TCA.

# Metodologías usadas

TF-IDF (Bag of Words)
Word2Vec
SVM (en desarrollo)
Random Forest (en desarrollo)

# Contenido del repositorio

tweets.csv -> dataset original
tweets_limpios.txt -> datos preprocesados
Código de métricas (Accuracy, Precision, Recall, F1, AUC)



"""
Documentación de Herramienta para detectar trastornos alimenticios a partir de un texto
Este módulo implementa un pipeline completo de Procesamiento de Lenguaje Natural (NLP)
para la detección de posibles señales de trastornos de la conducta alimentaria (TCA)
en publicaciones de redes sociales (tweets).

El sistema aborda el problema como una tarea de clasificación binaria:
* Clase 1: Presencia de señales de anorexia/TCA
* Clase 0: Ausencia de señales de riesgo

La evaluación del desempeño se realiza conforme al Protocolo de Evaluación-2,
utilizando el Área Bajo la Curva ROC (AUC) como métrica principal.
"""

# 1. IMPORTACIÓN DE LIBRERÍAS
Se importan librerías para:
* Preprocesamiento de texto (regex, stopwords)
* Representación vectorial (TF-IDF, Word2Vec)
* Entrenamiento de modelos supervisados (SVM, Random Forest)
* Evaluación de desempeño (Accuracy, Precision, Recall, F1-score, AUC-ROC)

# 2. FUNCIONES AUXILIARES
Se definen funciones para:
* Limpieza y normalización de texto
* Tokenización
* Detección basada en palabras clave (baseline)
Estas funciones permiten verificar el correcto funcionamiento del pipeline y son utilizadas tanto en el entrenamiento como en las pruebas de software.

# 3. PREPARACIÓN AUTOMÁTICA DEL DATASET
Se construye el dataset final de entrenamiento:
* Eliminación de valores nulos
* Generación de etiquetas binarias (0/1)
* Verificación de que existan ambas clases
Esta etapa garantiza la validez del conjunto de datos para entrenamiento supervisado.

# 4. DIVISIÓN TRAIN / TEST
El dataset se divide en conjuntos de entrenamiento y prueba de forma estratificada,
preservando la proporción de clases.
Esta decisión evita sesgos y cumple con buenas prácticas de validación.

# 5. FUNCIÓN GENERAL DE EVALUACIÓN
Se implementa una función genérica para:
* Entrenar modelos
* Calcular métricas estándar
* Calcular AUC-ROC a partir de scores continuos
Esta función asegura una comparación justa entre metodologías.

# 6. MODELOS BASADOS EN WORD2VEC
Cada tweet se representa como el promedio de los vectores Word2Vec de sus palabras.
Sobre esta representación se entrenan:
* Support Vector Machine (SVM)
* Random Forest (RF)

# 7. MODELOS BASADOS EN TF-IDF (BAG OF WORDS)
* Se utiliza TF-IDF con unigramas y bigramas para capturar términos y frases relevantes.
* Esta representación genera variables numéricas continuas de alta dimensión.
* Se entrenan los mismos clasificadores para comparación directa.

# 8. COMPARACIÓN FINAL DE MODELOS
* Los modelos se comparan utilizando F1-score y AUC-ROC.
* Se selecciona el modelo con mejor desempeño global y se exportan los resultados
* para análisis posterior y verificación del protocolo de evaluación.