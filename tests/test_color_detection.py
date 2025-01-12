import unittest
import cv2
from utils.color_detection import detect_colors

class TestColorDetection(unittest.TestCase):
    def test_detect_colors(self):
        image_path = 'images/test_image.jpg'
        result = detect_colors(image_path, (50, 100, 100), (70, 255, 255))
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, cv2.imread(image_path).shape)

if __name__ == '__main__':
    unittest.main()

