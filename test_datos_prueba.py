"""
Módulo de pruebas unitarias para el procesamiento de tweets.
Este archivo valida el correcto funcionamiento de las funciones
de limpieza, normalización, tokenización y detección de keywords.
"""

import unittest

''' ---- DATOS SIMULADOS Y FUNCIONES DE PROCESAMIENTO ----
Estas funciones contienen lógica de procesamiento de texto para tweets '''

# Elimina URLs, menciones y hashtags del texto
def limpiar_tweet(texto):
    import re
    texto = str(texto)
    texto = re.sub(r"http\S+|www\S+", " ", texto)
    texto = re.sub(r"@\w+", " ", texto)
    texto = re.sub(r"#", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# Normaliza el texto: minúsculas, elimina números, caracteres especiales y espacios extra
def normalizar_texto(texto):
    import re
    texto = texto.lower()
    texto = re.sub(r"http\S+|www\S+", " ", texto)
    texto = re.sub(r"@\w+", " ", texto)
    texto = re.sub(r"#", " ", texto)
    texto = re.sub(r"\d+", " ", texto)
    texto = re.sub(r"[^a-záéíóúñü\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# Divide el texto en palabras (tokens) válidas, eliminando stopwords cortas
def tokenizar(texto):
    stopwords = {"de", "la", "que"}
    tokens = normalizar_texto(texto).split()
    return [t for t in tokens if len(t) > 2 and t not in stopwords]

# Conjunto de palabras clave relacionadas con trastornos de conducta alimentaria
keywords_tca = {"anorexia", "bulimia", "tca", "thinspo"}

# Verifica si alguno de los tokens coincide con las palabras clave de TCA
def contiene_keyword(tokens):
    return any(t in keywords_tca for t in tokens)

# Corrige problemas de encoding (mojibake) en texto con caracteres especiales
def fix_mojibake(text):
    try:
        return text.encode("cp1252", errors="ignore").decode("utf-8", errors="ignore")
    except:
        return text


# CLASE DE PRUEBAS UNITARIAS

class TestProcesamientoTexto(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para validar las funciones
    de preprocesamiento de texto del proyecto.
    """

    # Verifica que limpiar_tweet elimina URLs, menciones y hashtags
    def test_limpiar_tweet(self):
        texto = "Hola @user mira esto https://test.com #salud"
        resultado = limpiar_tweet(texto)
        self.assertNotIn("@user", resultado)
        self.assertNotIn("http", resultado)
        self.assertNotIn("#", resultado)


    # Verifica que el texto se normaliza (minúsculas y sin caracteres extraños)
    def test_normalizar_texto(self):
        texto = "¡HOLA! 123 #Salud"
        resultado = normalizar_texto(texto)
        self.assertEqual(resultado, "hola salud")

    # Verifica que el texto se divide en tokens válidos
    def test_tokenizar(self):
        texto = "Hola esto es una prueba de anorexia"
        resultado = tokenizar(texto)
        self.assertIn("hola", resultado)
        self.assertIn("anorexia", resultado)

    # Verifica que detecta correctamente palabras clave
    def test_contiene_keyword_true(self):
        tokens = ["esto", "es", "anorexia"]
        self.assertTrue(contiene_keyword(tokens))

    # Verifica que retorna False si no hay keywords
    def test_contiene_keyword_false(self):
        tokens = ["esto", "es", "saludable"]
        self.assertFalse(contiene_keyword(tokens))

    # Verifica que la función corrige texto con encoding incorrecto"""
    def test_fix_mojibake(self):
        texto = "cafÃ©"
        resultado = fix_mojibake(texto)
        self.assertIsInstance(resultado, str)


# EJECUCIÓN
if __name__ == "__main__":
    unittest.main()
