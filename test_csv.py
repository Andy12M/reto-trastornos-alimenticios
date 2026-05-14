"""
Módulo de pruebas unitarias usando datos reales del archivo tweets.csv.
Valida el procesamiento completo del pipeline de texto.
"""

# Importar librerías
import unittest
import pandas as pd

# Importar funciones de procesamiento desde el módulo test_procesamiento
from test_datos_prueba import limpiar_tweet, normalizar_texto, tokenizar, contiene_keyword

class TestConCSV(unittest.TestCase):
    """
    Pruebas usando datos reales del dataset tweets.csv
    """

    @classmethod
    def setUpClass(cls):
        """
        Carga el dataset una sola vez antes de ejecutar las pruebas
        """
        # Lee el archivo CSV con los tweets, usando encoding latin1
        cls.df = pd.read_csv("tweets.csv", encoding="latin1")

        # Extrae la columna 'tweet_text', elimina valores nulos y toma solo los primeros 20
        cls.textos = cls.df["tweet_text"].dropna().head(20)

    def test_limpiar_tweet_csv(self):
        """
        Verifica que los tweets procesados no contengan URLs o menciones
        """
        # Itera sobre cada tweet en el conjunto de datos
        for texto in self.textos:
            # Limpia el tweet removiendo caracteres especiales
            limpio = limpiar_tweet(texto)
            self.assertNotIn("http", limpio)
            self.assertNotIn("@", limpio)

    def test_pipeline_tokenizacion(self):
        """
        Verifica que la tokenización genere listas válidas
        """
        # Itera sobre cada tweet en el conjunto de datos
        for texto in self.textos:
            tokens = tokenizar(texto)
            self.assertIsInstance(tokens, list)

    def test_tokens_no_vacios(self):
        """
        Verifica que algunos tweets generen tokens
        """
        # Tokeniza todos los textos y crea una lista con los resultados
        resultados = [tokenizar(t) for t in self.textos]
        # Verifica que al menos uno de los resultados tenga tokens (longitud > 0)
        self.assertTrue(any(len(t) > 0 for t in resultados))

    def test_contiene_keyword_csv(self):
        """
        Verifica si la función detecta al menos algunos casos positivos
        """
        resultados = []
        # Itera sobre cada tweet en el conjunto de datos
        for texto in self.textos:
            tokens = tokenizar(texto)
            # Verifica si el tweet contiene palabras clave y guarda el resultado
            resultados.append(contiene_keyword(tokens))
        # Verifica que al menos un tweet contenga una palabra clave
        self.assertTrue(any(resultados))


# EJECUCIÓN

if __name__ == "__main__":
    unittest.main()