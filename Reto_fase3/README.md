# Detección de TCA en Tweets con NLP y LLMs

# Autores
* Andrea Doce Murillo- A01799931
* Sandra Paulina Herrera Rebolledo- A01798452
* Ian Alexei Mtz. Armendáriz- A01753288


# Descripción del proyecto
Herramienta basada en técnicaas de procesamiento de Lenguaje Natural (NLP) y modelos de lenguaje de gran escala (LLMs) para detectar señales de trastornos de la conducta alimentaria (TCA) en tweets,

El sistema clasifica publicaciones como:
* Clase 0: No se detectan señales
* Clase 1: Posible señal de anorexia/TCA

# Objetivo
El objetivo del proyecto evolucionó en modelos basados en palabras clave a modelo capaces de poder comprendeer el contexto completo del lenguaje.

# Metodologías usadas

### Modelos de la fase anterior

* TF-IDF (Bag of Words)
* Word2Vec
* SVM (en desarrollo)
* Random Forest (en desarrollo)

### Modelos de fase 3

#### Transformers
* BERT embeddings + SVM
* RoBERTa embeddings + SVM


#### LLMs (Large Language Models)
* Ollama (Mistral, Gemma, Phi3)
* Cohere API
* Groq API

#### Técnicas aplicadas
* Zero-shot prompting
* Few-shot prompting
* Inferencia semántica (NLI)

# Pipeline del sistema

El sistema sigue un flujo estructurado: 

1. Entrada:
   * Dataset de tweets (CSV)

2. Limpieza de datos:
   * Eliminación de URLs, menciones, símbolos
   * Normalización del texto

3. División de datos:
   * Train / Test (estratificado)

4. Preprocesamiento:
   * Tokenización
   * Eliminación de stopwords
   * Normalización

5. Representación del texto:
   * TF-IDF
   * Word2Vec
   * Embeddings de transformers

6. Modelado:
   * Clasificadores tradicionales (SVM, RF, Logistic)
   * LLMs mediante prompts (Zero-shot / Few-shot)

7. Evaluación:
   * Accuracy
   * Precision
   * Recall
   * F1-score
   * AUC

8. Salida:
   * Comparación de modelos


# Evaluación del modelo

El desempeño de los modelos se evalúa utilizando:

* Accuracy: proporción de predicciones correctas
* Precision: qué tan precisas son las detecciones
* Recall: capacidad de detectar todos los casos reales 
* F1-score: balance entre precision y recall
* AUC-ROC: capacidad de distinguir entre clases

Se prioriza el Recall ya que se busca minimizar falsos negativos y es lo esencial del reto.


# Resultados y comparación

* Los modelos TF-IDF presentan buen desempeño en datasets pequeños
* Word2Vec muestra menor desempeño relativo
* Transformers mejoran la representación semántica
* LLMs presentan el mejor desempeño general

Análisis:
* LLMs logran Recall cercano a 1.0
* Detectan todos los casos reales
* Reducen falsos negativos a cero

# Implementación de LLMs

Los LLMs fueron utilizados mediante prompts:

### Zero-shot
Clasificación directa sin ejemplos previos

### Few-shot
Uso de ejemplos para guiar la respuesta del modelo

Con esto permitió evaluar su desempeño sin necesidad de entrenamiento supervisado.



# Comparación de implementación

### Modelos locales (Ollama)
* Mayor control del prompt
* Respuestas más consistentes
* Mejor estabilidad

### APIs (Groq, Cohere)
* Fácil integración
* Buen desempeño
* Dependencia de conexión y límites externos


# Validación y pruebas

Para asegurar que el sistema es confiable:

* Se generaron tablas comparativas con DataFrames
* Se validaron resultados mediante métricas consistentes
* Se incluyó manejo de errores y fallback en LLMs


# Contenido del archivo Reto_fase3

* tweets1.csv, tweets2.csv -> datasets
* tweets_limpios.txt -> datos preprocesados
* Reto_Fase3.ipynb -> Código completo de la fase 3
* Funciones de evaluación y métricas
* README.md


