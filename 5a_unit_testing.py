import unittest
from 2a_emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_returns_keys(self):
        result = emotion_detector("I am very happy today!")
        self.assertIsInstance(result, dict)
        self.assertIn("anger", result)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)
        self.assertIn("dominant_emotion", result)

    def test_emotion_detector_dominant_emotion(self):
        result = emotion_detector("I am very happy today!")
        self.assertIn(result["dominant_emotion"], ["anger", "disgust", "fear", "joy", "sadness"])

    def test_emotion_detector_empty_input(self):
        result = emotion_detector("")
        self.assertEqual(result["anger"], None)
        self.assertEqual(result["dominant_emotion"], None)

if __name__ == "__main__":
    unittest.main()
