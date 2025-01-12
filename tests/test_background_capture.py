import unittest
import cv2
from utils.background_capture import capture_background

class TestBackgroundCapture(unittest.TestCase):
    def test_capture_background(self):
        image_path = 'images/test_image.jpg'
        background = capture_background(image_path)
        self.assertIsNotNone(background)
        self.assertEqual(background.shape, cv2.imread(image_path).shape)

if __name__ == '__main__':
    unittest.main()

