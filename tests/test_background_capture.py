import unittest
from PIL import Image
from rembg import remove
import numpy as np
from IPython.display import display
from utils.background_capture import extract_background_and_foreground

class TestBackgroundCapture(unittest.TestCase):
    def test_capture_background(self):
        image_path = 'images/test_image.jpg'
        background, foreground = extract_background_and_foreground(image_path)
        self.assertIsNotNone(background)
        display(foreground_image)
        display(background_image)
        display(Image.open(image_path))

if __name__ == '__main__':
    unittest.main()

