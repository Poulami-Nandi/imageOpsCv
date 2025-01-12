import unittest
import cv2
from utils.edge_detection import canny_edge_detection
import numpy as np
from PIL import Image

class TestEdgeDetection(unittest.TestCase):


    def print_edges_as_image(self, edges):
        """Prints the edges returned by a Canny edge detection function as an image.

        Args:
            edges: A NumPy array representing the edges.
        """
        # Convert the NumPy array to a PIL Image.
        image = Image.fromarray(edges.astype(np.uint8), mode='L')
        # Display the image using Matplotlib.
        import matplotlib.pyplot as plt
        plt.imshow(image, cmap='gray')
        plt.title('Canny Edge Detection')
        plt.axis('off')  # Hide axes
        plt.show()

    def test_canny_edge_detection(self):
        edges = canny_edge_detection('images/test_image.jpg', 100, 200)
        self.assertIsNotNone(edges)
        self.assertEqual(edges.shape, cv2.imread('images/test_image.jpg', cv2.IMREAD_GRAYSCALE).shape)
        # print edges as image
        self.print_edges_as_image(edges)

if __name__ == '__main__':
    unittest.main()
