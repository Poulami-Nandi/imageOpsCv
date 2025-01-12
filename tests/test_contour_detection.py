import unittest
from utils.contour_detection import find_contours

class TestContourDetection(unittest.TestCase):
    def test_find_contours(self):
        contours = find_contours('images/test_image.jpg')
        self.assertIsInstance(contours, list)
        self.assertGreater(len(contours), 0)

if __name__ == '__main__':
    unittest.main()

