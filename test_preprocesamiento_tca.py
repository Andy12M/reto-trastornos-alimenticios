"""
Pruebas unitarias para funciones de limpieza, tokenización
y detección de posibles señales de anorexia/TCA.

Este archivo valida la lógica base utilizada antes del entrenamiento
de modelos de machine learning.
"""

import unittest
import re


# -------------------------------
# FUNCIONES DE PROCESAMIENTO
# -------------------------------

palabras_riesgo = {
    "anorexia", "anorexica", "anoréxica", "proana", "pro ana",
    "bulimia", "bulimica", "bulímica",
    "no comer", "sin comer", "ayunar", "ayuno",
    "calorias", "calorías", "bajar de peso", "perder peso",
    "thinspo", "odio mi cuerpo", "me siento gorda",
    "miedo a engordar", "vomitar", "laxantes"
}


def normalizar_texto(texto):
    """
    Limpia y normaliza texto para análisis NLP.
    """
    texto = str(texto).lower()
    texto = re.sub(r"http\S+|www\S+", " ", texto)
    texto = re.sub(r"@\w+", " ", texto)
    texto = re.sub(r"#", " ", texto)
    texto = re.sub(r"[^a-záéíóúñü\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def tokenizar_texto(texto):
    """
    Convierte un texto normalizado en una lista de tokens.
    """
    return normalizar_texto(texto).split()


def detectar_anorexia_tweet(tweet):
    """
    Detecta señales textuales relacionadas con anorexia/TCA.
    Regresa clasificación, puntaje y coincidencias encontradas.
    """
    texto = normalizar_texto(tweet)
    coincidencias = []

    for palabra in palabras_riesgo:
        palabra_normalizada = normalizar_texto(palabra)
        if palabra_normalizada in texto:
            coincidencias.append(palabra)

    puntaje = len(coincidencias)
    palabras_directas = {"anorexia", "anorexica", "anoréxica", "proana", "pro ana"}

    contiene_directa = any(normalizar_texto(p) in texto for p in palabras_directas)

    if puntaje >= 2 or contiene_directa:
        resultado = "Posible señal de anorexia/TCA"
    else:
        resultado = "No se detectan señales claras"

    return resultado, puntaje, coincidencias


# -------------------------------
# PRUEBAS UNITARIAS
# -------------------------------

class TestProcesamientoTCA(unittest.TestCase):
    """
    Pruebas para validar limpieza, tokenización y detección de señales.
    """

    def test_normalizar_elimina_url_menciones_hashtag(self):
        texto = "Hola @usuario revisa https://pagina.com #Salud"
        resultado = normalizar_texto(texto)

        self.assertNotIn("@usuario", resultado)
        self.assertNotIn("http", resultado)
        self.assertNotIn("#", resultado)
        self.assertIn("salud", resultado)

    def test_normalizar_convierte_a_minusculas(self):
        texto = "ANOREXIA y BULIMIA"
        resultado = normalizar_texto(texto)

        self.assertEqual(resultado, "anorexia y bulimia")

    def test_tokenizar_regresa_lista(self):
        texto = "Tengo miedo a engordar"
        tokens = tokenizar_texto(texto)

        self.assertIsInstance(tokens, list)
        self.assertIn("miedo", tokens)
        self.assertIn("engordar", tokens)

    def test_detectar_anorexia_directa(self):
        texto = "Estoy hablando sobre anorexia"
        resultado, puntaje, coincidencias = detectar_anorexia_tweet(texto)

        self.assertEqual(resultado, "Posible señal de anorexia/TCA")
        self.assertGreaterEqual(puntaje, 1)
        self.assertTrue(len(coincidencias) >= 1)

    def test_detectar_por_multiples_senales(self):
        texto = "Hoy quiero ayunar y contar calorias"
        resultado, puntaje, coincidencias = detectar_anorexia_tweet(texto)

        self.assertEqual(resultado, "Posible señal de anorexia/TCA")
        self.assertGreaterEqual(puntaje, 2)

    def test_no_detectar_texto_neutro(self):
        texto = "Hoy fui al parque y escuché música"
        resultado, puntaje, coincidencias = detectar_anorexia_tweet(texto)

        self.assertEqual(resultado, "No se detectan señales claras")
        self.assertEqual(puntaje, 0)
        self.assertEqual(coincidencias, [])


if __name__ == "__main__":
    unittest.main()
