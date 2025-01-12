import cv2
import numpy as np

def canny_edge_detection(image_path: str, threshold1: int, threshold2: int) -> np.ndarray:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges
