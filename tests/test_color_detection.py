import unittest
import cv2
from utils.color_detection import detect_colors
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class TestColorDetection(unittest.TestCase):
    def print_original_image_and_color(self, image_path, result_colors):
      """Prints the edges returned by a Canny edge detection function as an image.
      Args:
        edges: A NumPy array representing the edges.
      """
      image1 = mpimg.imread(image_path)
      # Create a figure with two subplots
      fig, axes = plt.subplots(1, 2, figsize=(10, 5))
      # Display the first image
      axes[0].imshow(image1)
      axes[0].axis('off')  # Hide axes
      axes[0].set_title('Actual image')
      # Display the second image
      # Convert the NumPy array to a PIL Image.
      axes[1].imshow(result_colors)
      axes[1].axis('off')  # Hide axes
      axes[1].set_title('Detected colors')
      plt.axis('off')  # Hide axes
      # Adjust layout
      plt.tight_layout()
      plt.show()

    def test_detect_colors(self):
        image_path = 'images/test_image.jpg'
        result = detect_colors(image_path, (0, 0, 0), (255, 255, 255))
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, cv2.imread(image_path).shape)
        self.print_original_image_and_color(image_path, result)

if __name__ == '__main__':
    unittest.main()

