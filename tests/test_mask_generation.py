import unittest
import cv2
from utils.mask_generation import generate_mask

class TestMaskGeneration(unittest.TestCase):
    def test_generate_mask(self):
        image_path = 'images/test_image.jpg'
        mask = generate_mask(image_path, (50, 100, 100), (70, 255, 255))
        self.assertIsNotNone(mask)
        self.assertEqual(mask.shape, cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).shape)

if __name__ == '__main__':
    unittest.main()
