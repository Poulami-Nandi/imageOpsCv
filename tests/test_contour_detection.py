import unittest
from utils.contour_detection import find_contours
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

class TestContourDetection(unittest.TestCase):

    def display_contours(self, image_path: str, contours):
        """
        Finds contours in an image and displays them on the original image.
        Args:
            image_path: Path to the input image file.
        """
        # Load the original image in color
        original_image = cv2.imread(image_path)
        # Draw contours on the original image
        cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)  
        # Display the image with contours using cv2_imshow
        cv2_imshow(original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_find_contours(self):
        image_path = 'images/test_image.jpg'
        contours = find_contours(image_path)
        self.assertIsInstance(contours, list)
        self.assertGreater(len(contours), 0)
        self.display_contours(image_path, contours)

if __name__ == '__main__':
    unittest.main()

