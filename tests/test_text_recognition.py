import unittest
from utils.text_recognition import recognize_text

class TestTextRecognition(unittest.TestCase):
    def test_recognize_text(self):
        text = recognize_text('images/handwritten_note.PNG')
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)
        print(text)

if __name__ == '__main__':
    unittest.main()

