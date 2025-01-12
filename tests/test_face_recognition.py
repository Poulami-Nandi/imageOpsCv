import unittest
from utils.face_recognition import find_face_locations_and_encodings

class TestFaceRecognition(unittest.TestCase):
    def test_recognize_face(self):
        face_locations, face_encodings = find_face_locations_and_encodings('images/human_face.jpg')

if __name__ == '__main__':
    unittest.main()

