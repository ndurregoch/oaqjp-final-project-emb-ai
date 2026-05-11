"""
Pruebas unitarias para el detector de emociones.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Pruebas para validar que el detector identifica correctamente
    la emocion dominante en diferentes textos.
    """

    def test_felicidad(self):
        """Valida una frase asociada con felicidad."""
        result = emotion_detector("I am very happy and joyful today")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_enojo(self):
        """Valida una frase asociada con enojo."""
        result = emotion_detector("I am extremely angry and furious about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_asco(self):
        """Valida una frase asociada con asco."""
        result = emotion_detector("This is disgusting and I completely hate it")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_tristeza(self):
        """Valida una frase asociada con tristeza."""
        result = emotion_detector("I am very sad and I want to cry")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_miedo(self):
        """Valida una frase asociada con miedo."""
        result = emotion_detector("I am very afraid and scared about what may happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()