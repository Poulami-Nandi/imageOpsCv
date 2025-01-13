import unittest
import cv2
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from utils.face_recognition import find_face_locations_and_encodings

class TestFaceRecognition(unittest.TestCase):
    def test_recognize_face(self):
        image_path = 'images/human_face.jpg'
        face_locations, face_encodings = find_face_locations_and_encodings(image_path)
        print("Number of faces detected:", len(face_locations))
        print("\nOriginal image")
        display(Image.open(image_path))
        # 1. Display Face Locations
        image = face_recognition.load_image_file(image_path)  
        pil_image = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_image)

        for (top, right, bottom, left) in face_locations:
          draw.rectangle(((left, top), (right, bottom)), outline="red", width=2)
        print("\nFace location in original image")
        display(pil_image) 

        print("\nFace encoding")
        # 2. Display Face Encodings (as grayscale images)
        for encoding in face_encodings:
          encoding_image = encoding.reshape(8, 16)  # Adjust dimensions if needed
          plt.imshow(encoding_image, cmap="gray")
          plt.show()

if __name__ == '__main__':
    unittest.main()

