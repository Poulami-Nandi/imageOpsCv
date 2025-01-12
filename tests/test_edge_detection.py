import unittest
import cv2
from utils.edge_detection import canny_edge_detection
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class TestEdgeDetection(unittest.TestCase):


    def print_edges_as_image(self, edges):
        """Prints the edges returned by a Canny edge detection function as an image.

        Args:
            edges: A NumPy array representing the edges.
        """
        # Convert the NumPy array to a PIL Image.
        image = Image.fromarray(edges.astype(np.uint8), mode='L')
        # Display the image using Matplotlib.
        plt.imshow(image, cmap='gray')
        plt.title('Canny Edge Detection')
        plt.axis('off')  # Hide axes
        plt.show()

    def print_edges_as_image(self, image_path, edges):
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
        image2 = Image.fromarray(edges.astype(np.uint8), mode='L')
        axes[1].imshow(image2, cmap='gray')
        axes[1].axis('off')  # Hide axes
        axes[1].set_title('Canny Edge Detection')
        #plt.title('Actual image vs Canny Edge Detection')
        plt.axis('off')  # Hide axes
        # Adjust layout
        plt.tight_layout()
        plt.show()

    def test_canny_edge_detection(self):
        edges = canny_edge_detection('images/test_image.jpg', 100, 200)
        self.assertIsNotNone(edges)
        self.assertEqual(edges.shape, cv2.imread('images/test_image.jpg', cv2.IMREAD_GRAYSCALE).shape)
        # print edges as image
        self.print_edges_as_image(edges)

if __name__ == '__main__':
    unittest.main()
